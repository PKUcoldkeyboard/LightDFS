import grpc
import sys
import time
from concurrent.futures import ThreadPoolExecutor

# 添加路径
sys.path.append('..')
# 数据服务器rpc
# import storageServer_pb2_grpc as st_pb2_grpc
# 管理服务器rpc
import MetaServer_pb2 as ma_pb2
import MetaServer_pb2_grpc as ma_pb2_grpc
# 参数文件
import parameter.parameter as parameter


class maServer(ma_pb2_grpc.managementServerServicer):
    def __init__(self):
        self.ip = parameter._MANAGEMENT_IP
        self.port = parameter._MANAGEMENT_PORT
        # 维护在线服务器信息
        self.serverList = list()
        # 维护上锁文件，数据结构为字典: path->id
        self.lockList = dict()
        print('Management Server is online')

    def offline(self):
        # 当还存在在线数据服务器时，发送警告
        if len(self.serverList):
            print('Warning: There are still online servers. Closing may cause exceptions.')
        print('Management Server is offline')

    def serverOnline(self, request, context):
        # 数据服务器上线，向管理器注册信息
        self.serverList.append(request)
        print('Storage Server:%d is online' % request.id)
        return ma_pb2.ma_reply(done=1)

    def serverOffline(self, request, context):
        # 数据服务器下线，向管理器注销信息
        remove_id = request.id
        for server in self.serverList:
            if server.id == remove_id:
                remove_server = server
                break
        self.serverList.remove(remove_server)
        print('Storage Server:%d is offline' % request.id)
        return ma_pb2.ma_reply(done=1)

    def getServerList(self, request, context):
        # 获取在线数据服务器信息
        server_list = list()
        for server in self.serverList:
            server_list.append(server)
        return ma_pb2.serverList(list=server_list)

    def lockFile(self, request, context):
        # 给文件上锁
        print('Lock: ' + request.filePath)
        if request.filePath in self.lockList:
            finish = 0
            if request.clientId == self.lockList[request.filePath]:
                reply = 'Alreay lock this file'
            else:
                reply = 'This file is locked by other client'
        else:
            finish = 1
            self.lockList[request.filePath] = request.clientId
            reply = 'Successfully lock the file, do not forget to unlock it after used'
        return ma_pb2.lockReply(done=finish, info=reply)

    def unlockFile(self, request, context):
        # 给文件解锁
        # 给文件上锁
        print('Unlock: ' + request.filePath)
        if request.filePath in self.lockList:
            if request.clientId == self.lockList[request.filePath]:
                finish = 1
                del self.lockList[request.filePath]
                reply = 'Successfully unlock the file'
            else:
                reply = 'This file is locked by other client, you can`t unlock it'
        else:
            finish = 1
            reply = 'This file isn`t locked by any client'
        return ma_pb2.lockReply(done=finish, info=reply)


if __name__ == "__main__":
    # 开启管理服务器
    ma_server = maServer()
    server = grpc.server(ThreadPoolExecutor(max_workers=5))
    ma_pb2_grpc.add_managementServerServicer_to_server(ma_server, server)
    server.add_insecure_port(parameter._MANAGEMENT_IP + ':' + parameter._MANAGEMENT_PORT)
    server.start()
    try:
        while True:
            time.sleep(parameter._ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        # 管理服务器下线
        ma_server.offline()
        server.stop(0)