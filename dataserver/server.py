import grpc
import os
import sys
import shutil
import signal
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'nameserver'))
from concurrent import futures
from utils.logger import configure_logger
from utils.settings import DFS_SETTINGS
from utils.snowflake import getId
import nameserver_pb2_grpc as ns_grpc
import nameserver_pb2 as ns_pb2
import dataserver_pb2_grpc as ds_grpc
import dataserver_pb2 as ds_pb2


class DataServerServicer(ds_grpc.DataServerServicer):
    def __init__(self, id=None, host=None, port=None, data_dir=None):
        self.id = id
        self.host = host
        self.port = port
        self.data_dir = data_dir

        logger_path = DFS_SETTINGS['LOG_CONFIG']['LOG_DIR'] + \
            f'dataserver_{self.id}.log'
        logger_level = DFS_SETTINGS['LOG_CONFIG']['LOG_LEVEL']
        log_to_console = DFS_SETTINGS['LOG_CONFIG']['LOG_TO_CONSOLE']
        log_to_file = DFS_SETTINGS['LOG_CONFIG']['LOG_TO_FILE']
        self.logger = configure_logger(
            log_to_console=log_to_console, log_file_path=logger_path, log_to_file=log_to_file, level=logger_level)
        self.logger.info(
            f"DataServer {self.host} is starting, listen port: {self.port}")

        # 如果数据目录不存在则创建
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        # 连接NameServer
        channel_string = f'{DFS_SETTINGS["NAMESERVER"]["HOST"]}:{DFS_SETTINGS["NAMESERVER"]["PORT"]}'
        channel = grpc.insecure_channel(channel_string)
        self.stub = ns_grpc.NameServerStub(channel)

        # 上线请求
        response = self.stub.RegisterDataServer(
            ns_pb2.DataServerInfo(id=self.id, host=self.host, port=self.port))
        if not response.success:
            self.logger.error(response.message)
        else:
            self.logger.info(response.message)

    def CreateFile(self, request, context):
        self.logger.info(f"touch {request.path} - {request.sequence_id}")
        file_path = f'{self.data_dir}{request.path}'
        try:
            with open(file_path, 'w') as f:
                pass
            self.stub.AddFile(ns_pb2.FileInfo(absolute_path=request.path,
                              size=0, is_dir=False, ctime=request.ctime, mtime=request.mtime))
        except grpc.RpcError:
            self.logger.error("Connect to NameServer error!")
            # 回滚操作
            if os.path.exists(file_path):
                os.remove(file_path)
            return ds_pb2.BaseResponse(success=0, message='Connect to NameServer error!', sequence_id=request.sequence_id)
        except Exception as e:
            self.logger.error(e)
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)

        return ds_pb2.BaseResponse(success=1, message='Create file successfully! ', sequence_id=request.sequence_id)

    def DeleteFile(self, request, context):
        self.logger.info(f"rm {request.path} - {request.sequence_id}")
        file_path = f'{self.data_dir}{request.path}'
        recursive = request.recursive
        try:
            if not os.path.exists(file_path):
                return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request.sequence_id)

            if recursive:
                os.removedirs(file_path)
            else:
                if os.path.isdir(file_path):
                    return ds_pb2.BaseResponse(success=0, message='Can not delete a dir!', sequence_id=request.sequence_id)
                os.remove(file_path)

        except Exception as e:
            self.logger.error(e)
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)

        return ds_pb2.BaseResponse(success=1, message='Delete file successfully! ', sequence_id=request.sequence_id)

    def ReadFile(self, request, context):
        self.logger.info(f"cat {request.path} - {request.sequence_id}")
        file_path = f'{self.data_dir}{request.path}'
        try:
            if not os.path.exists(file_path):
                return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request.sequence_id)

            if os.path.isdir(file_path):
                return ds_pb2.BaseResponse(success=0, message='Path is not a file!', sequence_id=request.sequence_id)

            with open(file_path, 'r') as f:
                content = f.read()
        except Exception as e:
            self.logger.error(e)
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)

        return ds_pb2.ReadFileResponse(success=1, content=content, sequence_id=request.sequence_id)

    def CreateDirectory(self, request, context):
        self.logger.info(f"mkdir {request.path} - {request.sequence_id}")
        dir_path = f'{self.data_dir}{request.path}'
        parent = request.parent
        if not parent and not os.path.exists(os.path.dirname(dir_path)):
            return ds_pb2.BaseResponse(success=0, message='Parent directory not found!', sequence_id=request.sequence_id)

        try:
            os.makedirs(dir_path)
        except Exception as e:
            self.logger.error(e)
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)

        return ds_pb2.BaseResponse(success=1, message='Create directory successfully! ', sequence_id=request.sequence_id)

    def RenameFile(self, request, context):
        self.logger.info(
            f"mv {request.src} {request.dst} - {request.sequence_id}")
        src = f'{self.data_dir}{request.src}'
        dst = f'{self.data_dir}{request.dst}'
        # 判断文件是否存在
        if not os.path.exists(src):
            return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request.sequence_id)

        try:
            os.rename(src, dst)
        except Exception as e:
            self.logger.error(e)
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)

        return ds_pb2.BaseResponse(success=1, message='Rename file successfully! ', sequence_id=request.sequence_id)

    def CopyFile(self, request, context):
        self.logger.info(
            f"cp {request.src} {request.dst} - {request.sequence_id}")
        src = f'{self.data_dir}{request.src}'
        dst = f'{self.data_dir}{request.dst}'
        recursive = request.recursive
        # 判断文件是否存在
        if not os.path.exists(src) or not os.path.exists(os.path.dirname(dst)):
            return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request.sequence_id)

        try:
            if recursive:
                shutil.copytree(src, dst)
            else:
                shutil.copy(src, dst)
        except Exception as e:
            self.logger.error(e)
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)
        return ds_pb2.BaseResponse(success=1, message='Copy file successfully! ', sequence_id=request.sequence_id)

    def UploadFile(self, request_iterator, context):
        self.logger.info(f"upload file... - {request_iterator.sequence_id}")
        path = f'{self.data_dir}{request_iterator.path}'
        content = request_iterator.content
        # 判断路径是否存在
        if not os.path.exists(os.path.dirname(path)):
            return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request_iterator.sequence_id)

        # 写入文件bytes
        try:
            with open(path, 'wb') as f:
                f.write(content)

            # 获取所有副本服务器的地址
            while True:
                response = self.stub.GetDataServerList(ns_pb2.empty(e=0))
                break

            for server in response.dataServerInfoList:
                if server.id == self.id:
                    continue

                # 建立连接
                temp_channel = grpc.insecure_channel(
                    f'{server.host}:{server.port}')
                temp_stub = ds_grpc.DataServerStub(temp_channel)

                response = temp_stub.UploadFileWithoutSync(ds_pb2.UploadFileRequest(
                    path=request_iterator.path, content=request_iterator.content, sequence_id=getId()))

        except grpc.RpcError as e:
            return ds_pb2.BaseResponse(success=0, message='RPC Connection Timeout!', sequence_id=request_iterator.sequence_id)
        except Exception as e:
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request_iterator.sequence_id)
        return ds_pb2.BaseResponse(success=1, message='Upload file successfully! ', sequence_id=request_iterator.sequence_id)

    def UploadFileWithoutSync(self, request_iterator, context):
        self.logger.info(
            f"upload file without sync... - {request_iterator.sequence_id}")
        path = f'{self.data_dir}{request_iterator.path}'
        content = request_iterator.content
        # 判断路径是否存在
        if not os.path.exists(os.path.dirname(path)):
            return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request_iterator.sequence_id)

        # 写入文件bytes
        try:
            with open(path, 'wb') as f:
                f.write(content)
        except Exception as e:
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request_iterator.sequence_id)
        return ds_pb2.BaseResponse(success=1, message='Upload file successfully! ', sequence_id=request_iterator.sequence_id)

    def DownloadFile(self, request, context):
        self.logger.info(f"download file... - {request.sequence_id}")
        path = f'{self.data_dir}{request.path}'
        # 判断路径是否存在
        if not os.path.exists(path):
            return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request.sequence_id)

        # 读取文件bytes
        try:
            with open(path, 'rb') as f:
                content = f.read()
        except Exception as e:
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)
        return ds_pb2.DownloadFileResponse(success=1, content=content, sequence_id=request.sequence_id)

    
    def NotifyOffline(self, request, context):
        self.logger.info(f"notify offline...")
        # 收到消息后，关闭服务器
        os.kill(os.getpid(), signal.SIGINT)
        return ds_pb2.BaseResponse(success=1, message='Notify offline successfully! ', sequence_id=request.sequence_id)

def start_server():
    id = getId()
    host = DFS_SETTINGS['DATASERVER']['HOST']
    port = DFS_SETTINGS['DATASERVER']['PORT']
    data_dir = DFS_SETTINGS['DATASERVER']['DATA_DIR']

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ds_grpc.add_DataServerServicer_to_server(
        DataServerServicer(id, host, port, data_dir), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        # 下线通知
        channel = grpc.insecure_channel(
            f'{DFS_SETTINGS["NAMESERVER"]["HOST"]}:{DFS_SETTINGS["NAMESERVER"]["PORT"]}')
        stub = ns_grpc.NameServerStub(channel)
        stub.LogoutDataServer(ns_pb2.DataServerInfo(
            id=id, host=host, port=port))


if __name__ == "__main__":
    start_server()
