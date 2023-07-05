import grpc
import os
import sys
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import dataserver_pb2_grpc as ds_grpc
import dataserver_pb2 as ds_pb2
from concurrent import futures
from utils.logger import configure_logger
from utils.settings import DFS_SETTINGS


class DataServerServicer(ds_grpc.DataServerServicer):
    def __init__(self, host=None, port=None, data_dir=None):
        self.logger = configure_logger()
        self.host = host
        self.port = port
        self.data_dir = data_dir
        self.logger.info(f"DataServer {self.host} is starting, listen port: {self.port}")
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def ListFile(self, request, context):
        self.logger.info(f"ls {request.path} - {request.sequence_id}")
        # 客户端限制了path的格式，传入的一定是绝对路径，所以直接拼接即可
        file_path = f'{self.data_dir}{request.path}'
        
        # 判断文件是否存在
        if not os.path.exists(file_path):
            return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request.sequence_id)
        
        if os.path.isfile(file_path):
            return ds_pb2.BaseResponse(success=0, message='Path is not a directory!', sequence_id=request.sequence_id)
        
        files = os.listdir(file_path)
        return ds_pb2.ListFileResponse(success=1, files=files, sequence_id=request.sequence_id)
    
    
    def CreateFile(self, request, context):
        self.logger.info(f"touch {request.path} - {request.sequence_id}")
        file_path = f'{self.data_dir}{request.path}'
        try:
            with open(file_path, 'w') as f:
                pass
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
        self.logger.info(f"mv {request.src} {request.dst} - {request.sequence_id}")
        src = f'{self.data_dir}{request.src}'
        dst = f'{self.data_dir}{request.dst}'
        # 判断文件是否存在
        if not os.path.exists(src) or not os.path.exists(os.path.dirname(dst)):
            return ds_pb2.BaseResponse(success=0, message='Path not found!', sequence_id=request.sequence_id)
        
        try:
            os.rename(src, dst)
        except Exception as e:
            self.logger.error(e)
            return ds_pb2.BaseResponse(success=0, message=str(e), sequence_id=request.sequence_id)
        
        return ds_pb2.BaseResponse(success=1, message='Rename file successfully! ', sequence_id=request.sequence_id)
        

def start_server():
    host = DFS_SETTINGS['DATASERVER']['HOST']
    port = DFS_SETTINGS['DATASERVER']['PORT']
    data_dir = DFS_SETTINGS['DATASERVER']['DATA_DIR']
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ds_grpc.add_DataServerServicer_to_server(DataServerServicer(host, port, data_dir), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    start_server()
