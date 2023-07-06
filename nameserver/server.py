import grpc
import os
import sys
import db
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nameserver_pb2 as ns_pb2
import nameserver_pb2_grpc as ns_pb2_grpc
from concurrent import futures
from models import DataServer
from utils.settings import DFS_SETTINGS
from utils.snowflake import getId
from utils.jwt import JWT
from utils.logger import configure_logger


class NameServerServicer(ns_pb2_grpc.NameServerServicer):
    def __init__(self, id, host, port):
        self.id = id
        self.host = host
        self.port = port

        logger_path = DFS_SETTINGS['LOG_CONFIG']['LOG_DIR'] + \
            f'nameserver_{self.id}.log'
        logger_level = DFS_SETTINGS['LOG_CONFIG']['LOG_LEVEL']
        log_to_console = DFS_SETTINGS['LOG_CONFIG']['LOG_TO_CONSOLE']
        log_to_file = DFS_SETTINGS['LOG_CONFIG']['LOG_TO_FILE']

        self.logger = configure_logger(
            log_to_console=log_to_console, log_file_path=logger_path, log_to_file=log_to_file, level=logger_level)
        self.trie = db.get_trie()
        if self.trie is None:
            self.logger.error('Trie is None')
        self.logger.info(
            f"NameServer is starting, listen port: {self.port}"
        )
        self.DataServerList = []
        self.ReadLockDist = {}
        self.WriteLockDist = {}
        self.logger.info("NameServer is started")

    def stop(self):
        self.logger.info("NameServer is stopping")
        self.logger.info("NameServer is stopped")

    def ListFile(self, request, context):
        # 1. 判断用户是否已经登录
        try:
            # 2. 判断目录是否存在
            if not self.trie.check_dir(request.path):
                return ns_pb2.ListFileResponse(success=0, files=[])
            # 3. 获取目录下的文件列表
            files = self.trie.list_dir(request.path)
            return ns_pb2.ListFileResponse(success=1, files=files)
        except Exception as e:
            self.logger.error(e)
            return ns_pb2.ListFileResponse(success=0, files=[])

    def RegisterDataServer(self, request, context):
        self.DataServerList.append(DataServer(
            request.id, request.host, request.port))
        self.logger.info(f"DataServer {request.id} is online")
        return ns_pb2.Response(success=1, message="Register successfully!")

    def GetDataServerList(self, request, context):
        return ns_pb2.GetDataServerListResponse(success=1, message="Get DataServer list successfully!",
                                                data_server_list=self.DataServerList)

    def LogoutDataServer(self, request, context):
        self.DataServerList = list(
            filter(lambda x: x.did != request.id, self.DataServerList))
        self.logger.info(f"DataServer {request.id} is offline")
        return ns_pb2.Response(success=1, message="Logout successfully!")

    def RegisterUser(self, request, context):
        success, message = db.register_user(request.username, request.password)
        return ns_pb2.Response(success=success, message=message)

    def Login(self, request, context):
        # 1. 判断用户是否已经登录
        metadata = dict(context.invocation_metadata())
        jwt = metadata.get('jwt')[0]
        
        if self.verify_token(jwt):
            return ns_pb2.Response(success=0, message="User already login!")
        
        success, message = db.login(request.username, request.password)
        if success:
            jwt = self.gen_token(request.username)
            context.set_trailing_metadata(('jwt', jwt))
            return ns_pb2.Response(success=1, message=message)
        return ns_pb2.Response(success=0, message=message)

    def LockFile(self, request, context):
        # 1. 判断用户是否已经登录
        metadata = dict(context.invocation_metadata())
        jwt = metadata.get('jwt')
        
        if not self.verify_token(jwt):
            return ns_pb2.Response(success=0, message="User already login!")
        
        # 获得文件路径和锁的类型
        file_path = request.filepath
        lock_type = request.lock_type
        # 2. 若加读锁
        if lock_type == 0:
            # 2.1 判断该文件是否已经加了写锁
            if file_path in self.WriteLockDist:
                return ns_pb2.Response(success=0, message="File already locked!")
            # 2.2 若没有加写锁，则加读锁
            if file_path not in self.ReadLockDist:
                self.ReadLockDist[file_path] = 1
            else:
                self.ReadLockDist[file_path] += 1
            return ns_pb2.Response(success=1, message="Lock file successfully!")
        # 3. 若加写锁
        elif lock_type == 1:
            # 3.1 判断该文件是否已被加锁
            if file_path in self.ReadLockDist or file_path in self.WriteLockDist:
                return ns_pb2.Response(success=0, message="File already locked!")
            # 3.2 若没有加锁，则加写锁
            self.WriteLockDist[file_path] = 1
            return ns_pb2.Response(success=1, message="Lock file successfully!")

    def UnlockFile(self, request, context):
        # 1. 判断用户是否已经登录
        metadata = dict(context.invocation_metadata())
        jwt = metadata.get('jwt')
        
        if not self.verify_token(jwt):
            return ns_pb2.Response(success=0, message="User already login!")
        # 获得文件路径和锁的类型
        file_path = request.filepath
        lock_type = request.lock_type
        # 2. 若解读锁
        if lock_type == 0:
            # 2.1 判断该文件是否已经加了读锁
            if file_path not in self.ReadLockDist:
                return ns_pb2.Response(success=0, message="File not locked!")
            # 2.2 解读锁
            if file_path in self.ReadLockDist:
                self.ReadLockDist[file_path] -= 1
                if self.ReadLockDist[file_path] == 0:
                    del self.ReadLockDist[file_path]
            return ns_pb2.Response(success=1, message="Unlock file successfully!")
        # 3. 若解写锁
        elif lock_type == 1:
            # 3.1 判断该文件是否已被加锁
            if file_path not in self.WriteLockDist:
                return ns_pb2.Response(success=0, message="File not locked!")
            # 3.2 解写锁
            del self.WriteLockDist[file_path]
            return ns_pb2.Response(success=1, message="Unlock file successfully!")

    def AddFile(self, request, context):
        success, message = db.create_file(
            request.absolute_path, request.size, request.is_dir, request.ctime, request.mtime)
        if success:
            return ns_pb2.Response(success=1, message=message)
        return ns_pb2.Response(success=0, message=message)

    def DeleteFile(self, request, context):
        success, message = db.delete_file(request.absolute_path)
        if success:
            return ns_pb2.Response(success=1, message=message)
        return ns_pb2.Response(success=0, message=message)

    def ModifyFile(self, request, context):
        if request.old_absolute_path != request.new_absolute_path:
            file = db.get_file(request.old_absolute_path)
            db.delete_file(request.old_absolute_path)
            success, message = db.create_file(request.new_absolute_path, file.size, file.is_dir,
                                              file.ctime, request.mtime)
            if success:
                return ns_pb2.Response(success=1, message=message)
            return ns_pb2.Response(success=0, message=message)
        else:
            success, message = db.update_file(absolute_path=request.new_absolute_path,
                                              size=request.new_size, mtime=request.mtime)
            if success:
                return ns_pb2.Response(success=1, message=message)
            return ns_pb2.Response(success=0, message=message)

    def GetFileInfo(self, request, context):
        file = db.get_file(request.absolute_path)
        if file is None:
            return ns_pb2.Response(success=0, message="File not exist!")
        return ns_pb2.FileInfoResponse(success=1, message="Get file info successfully!",
                                       size=file.size, is_dir=file.is_dir, ctime=file.ctime, mtime=file.mtime)

    def CheckCache(self, request, context):
        file = db.get_file(request.filepath)
        if file.mtime > request.mtime:
            return ns_pb2.Response(success=0, message="File has been modified!")
        return ns_pb2.Response(success=1, message="File is up to date!")
    
    # 针对用户名和密码生成token
    def gen_token(username):
        payload = {  # 生成payload
            'username': username,
        }
        jwt = JWT(DFS_SETTINGS['JWT_SECRET'])
        return jwt.encode(payload)


    def verify_token(token):
        if token is None:
            return False
        
        jwt = JWT(DFS_SETTINGS['JWT_SECRET'])
        decoded_token = jwt.decode(token)
        # check
        username = decoded_token['username']
        user = db.get_user(username)
        if not user:
            return False

        return True


if __name__ == "__main__":
    id = getId()
    host = DFS_SETTINGS['NAMESERVER']['HOST']
    port = DFS_SETTINGS['NAMESERVER']['PORT']
    Nserver = NameServerServicer(id, host, port)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ns_pb2_grpc.add_NameServerServicer_to_server(Nserver, server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        Nserver.stop()
        server.stop(0)
