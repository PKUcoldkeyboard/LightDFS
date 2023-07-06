import grpc
import os
import sys
import db
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger import configure_logger
from models import DataServer
from concurrent import futures
import nameserver_pb2_grpc as ns_pb2_grpc
import nameserver_pb2 as ns_pb2

class NameServerServicer(ns_pb2_grpc.NameServerServicer):
    def __init__(self, host, port):
        self.logger = configure_logger()
        self.trie, msg = db.get_trie()
        if self.trie is None:
            self.logger.error(msg)
        self.host = host
        self.port = port
        self.logger.info(
            f"NameServer is starting, listen port: {self.port}"
        )
        self.DataServerList = []
        self.ReadLockDist = {}
        self.WriteLockDist = {}
        self.OnlineUserDist = {}
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
        if request.username in self.OnlineUserDist:
            return ns_pb2.Response(success=0, message="User already login!")
        success, message = db.login(request.username, request.password)
        if success:
            self.OnlineUserDist[request.username] = 1
            return ns_pb2.Response(success=1, message=message)
        return ns_pb2.Response(success=0, message=message)

    def Logout(self, request, context):
        # 1. 判断用户是否已经登录
        if request.username not in self.OnlineUserDist:
            return ns_pb2.Response(success=0, message="User not login!")
        del self.OnlineUserDist[request.username]
        return ns_pb2.Response(success=1, message="Logout successfully!")

    def LockFile(self, request, context):
        # 1. 判断用户是否已经登录
        if request.username not in self.OnlineUserDist:
            return ns_pb2.Response(success=0, message="User not login!")
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
        if request.username not in self.OnlineUserDist:
            return ns_pb2.Response(success=0, message="User not login!")
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


if __name__ == "__main__":
    host = "localhost"
    port = 9000
    Nserver = NameServerServicer(host, port)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ns_pb2_grpc.add_NameServerServicer_to_server(Nserver, server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        Nserver.stop()
        server.stop(0)
