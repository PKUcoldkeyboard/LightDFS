import grpc
import nameserver_pb2 as ns_pb2
import nameserver_pb2_grpc as ns_pb2_grpc
from concurrent import futures
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger import configure_logger
from models import DataServer
import db

class NameServerServicer(ns_pb2_grpc.NameServerServicer):
    def __init__(self, host, port):
        self.logger = configure_logger()
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

    def RegisterDataServer(self, request, context):
        self.DataServerList.append(DataServer(request.id, request.host, request.port))
        self.logger.info(f"DataServer {request.id} is online")
        return ns_pb2.Response(success=1, message="Register successfully!")

    def GetDataServerList(self, request, context):
        return ns_pb2.GetDataServerListResponse(success=1, message="Get DataServer list successfully!",
                               data_server_list=self.DataServerList)

    def LogoutDataServer(self, request, context):
        self.DataServerList = list(filter(lambda x: x.did != request.id, self.DataServerList))
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
            return ns_pb2.Response(success=success, message=message)
        return ns_pb2.Response(success=success, message=message)

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

if __name__ == "__main__":
    host = "localhost"
    port = 9000
    Nserver = NameServerServicer(host, port)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ns_pb2_grpc.add_NameServerServicer_to_server(Nserver, server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        Nserver.stop()
        server.stop(0)
