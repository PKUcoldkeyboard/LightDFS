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
        self.DataServerList = list(filter(lambda x: x.id != request.id, self.DataServerList))
        self.logger.info(f"DataServer {request.id} is offline")
        return ns_pb2.Response(success=1, message="Logout successfully!")

    def RegisterUser(self, request, context):
        success, message = db.register_user(request.username, request.password)
        return ns_pb2.Response(success=success, message=message)

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
