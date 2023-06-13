import grpc
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
# 添加路径
sys.path.append('..')
sys.path.append('../DataServer')
sys.path.append('../MetaServer')
# 数据服务器rpc
import DataServer.DataServer_pb2 as st_pb2
import DataServer.DataServer_pb2_grpc as st_pb2_grpc
# 管理服务器rpc
import MetaServer.MetaServer_pb2 as ma_pb2
import MetaServer.MetaServer_pb2_grpc as ma_pb2_grpc
# 参数文件
import parameter.parameter as parameter

class Client():
    def __init__(self, id):
        self.id = id
        self.root_path = parameter._ROOT_PATH+'/DATASTORE/client_%d/'%(id)
        self.cur_path = ''
        self.openFile = list() # 已打开文件列表
        # 创建数据的主文件夹作为用户的缓存
        if not os.path.exists(self.root_path):
            os.mkdir(self.root_path)
        # 连接到管理服务器
        print('Connect with the Management Server ...')
        maChannel = grpc.insecure_channel(parameter._MANAGEMENT_IP+':'+parameter._MANAGEMENT_PORT)
        self.maStub = ma_pb2_grpc.managementServerStub(maChannel)
        # 选择存储服务器
        self.selectStorageServer()

    def selectStorageServer(self):
        try:
            response = self.maStub.getServerList(ma_pb2.empty(e = 1))
            print('Please choose a storage server:')
            print('***********************************')
            for info in response.list:
                print('Server %d   ip:'%info.id+info.ip+'   port:%d'%info.port)
            print('***********************************')
            while True:
                success = False
                choose = int(input('The id of server to connect:'))
                for info in response.list:
                    if info.id == choose:
                        serverIp = info.ip
                        serverPort = info.port
                        success = True
                        break
                if success:
                    break
                print('The idx of server is not online.')
            stChannel = grpc.insecure_channel(serverIp+':'+str(serverPort))
            self.stStub = st_pb2_grpc.storageServerStub(stChannel)
            self.server_root_path = parameter._ROOT_PATH + '/DATASTORE/storage_%d/'%(choose)
            print('Client %d'%self.id + ' successfully startup and connect with server %d'%choose)
        except Exception as e:
            print(e.args)
            print('Client startup failed.')

    def ls(self):
        response = self.stStub.ls(st_pb2.file_path(path = self.cur_path))
        print(response.list)

    def mkdir(self, fileName):
        response = self.stStub.mkdir(st_pb2.file_path(path = self.cur_path+fileName))
        if response.done:
            print('Successfully create dir:%s.'%fileName)
        else:
            print('Create failed.')

    def rm(self, fileName):
        response = self.stStub.synDelete(st_pb2.file_path(path = self.cur_path+fileName))
        if response.done:
            path = self.root_path+self.cur_path+fileName
            if os.path.exists(path):
                os.remove(path)
            print('Successfully delete dir:%s.'%fileName)
        else:
            print('Delete failed.')

    def download(self, fileName):
        try:
            response = self.stStub.download(st_pb2.file_path(path = self.cur_path+fileName))
            # 二进制打开文件用于写入
            path = self.root_path + self.cur_path
            # 本地文件不存在就创建
            if not os.path.exists(path):
                os.mkdir(path)
            with open(path+fileName, 'wb') as f:
                for i in response:
                    f.write(i.buffer)
            print('Successfully download the file.')
        except Exception as e:
            print(e.args)
            print('Download failed.')

    def create(self, fileName):
        path = self.root_path + self.cur_path
        # 本地文件不存在就创建
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path+fileName, 'w') as f:
            try:
                while True:
                    msg = input()
                    f.write(msg)
            except KeyboardInterrupt:
                # 结束写入
                f.close()
        print('Successfully create file:'+fileName)
        self.upload(fileName)

    def getBuffer(self, rPath, path):
        # 根据文件相对路径和本地绝对路径返回流式数据
        with open(path, 'rb') as f:
            buf = f.read(parameter._BUFFER_SIZE)
            yield st_pb2.upload_file(path = rPath, buffer = buf)

    def upload(self, fileName):
        try:
            path = self.root_path + self.cur_path + fileName # 本地绝对路径
            rPath = self.cur_path + fileName # 相对路径
            if os.path.exists(path):
                response = self.stStub.synUpload(self.getBuffer(rPath, path))
                print('Successfully upload the file.')
            else:
                print('Can`t find this file.')
        except Exception as e:
            print(e.args)
            print('Upload failed.')

    def cd(self, fold):
        response = self.stStub.ls(st_pb2.file_path(path = self.cur_path))
        path = self.server_root_path + self.cur_path+fold
        if fold in response.list and os.path.isdir(path):
            # 成功进入文件夹
            self.cur_path += fold + '/'
        else:
            print('Can`t enter this fold.')


    def cdBack(self):
        if (self.cur_path != ''):
            self.cur_path = os.path.dirname(self.cur_path[:-1])+'/'
            if self.cur_path == '/':
                self.cur_path = ''
        else:
            print('Alreay in root dir.')

    def open(self, fileName):
        response = self.stStub.ls(st_pb2.file_path(path = self.cur_path))
        if fileName in response.list and os.path.isfile(self.server_root_path+self.cur_path+fileName):
            # 确定文件存在且是文件而非文件夹
            # 对文件进行上锁
            response = self.maStub.lockFile(ma_pb2.lockInfo(clientId=self.id, filePath=self.cur_path+fileName))
            if response.done == 1:
                # 成功上锁
                self.openFile.append(self.cur_path+fileName)
                # 下载文件到本地
                self.download(fileName)
                print('Successfully open: '+fileName)
                # 输出文件信息
                print('************FILE CONTENT*************')
                with open(self.root_path+self.cur_path+fileName, 'r') as f:
                    buf = f.read()
                    print(buf)
                f.close()
                print('*************************************')
            else:
                print(response.info)
        else:
            print('Can`t find this file.')

    def close(self, fileName):
        path = self.cur_path + fileName
        if path in self.openFile:
            self.openFile.remove(path)
            # 上传文件
            self.upload(fileName)
            # 解锁文件
            response = self.maStub.unlockFile(ma_pb2.lockInfo(clientId=self.id, filePath=self.cur_path+fileName))
            if response.done == 1:
                os.remove(self.root_path+self.cur_path+fileName)
                print('Successfully close: '+fileName)
            else:
                print(response.info)
        else:
            print('You haven`t open this file.')

    def help(self):
        print('client ID: %d'%(self.id))
        print("------------------COMMAND LIST------------------")
        print("ls: list file directories")
        print("cd: change current path")
        print("cd..: back to previous path")
        print("create: create files locally")
        print("open: open files")
        print("close: close files")
        print("mkdir: create folder")
        print("rm: delete files")
        print("------------------------------------------------")


# 启动客户端
def startClient(id):
    client = Client(id)
    while True:
        print('$'+client.cur_path+'>', end = '')
        command = input().split()
        if len(command) == 0:
            continue
        elif command[0] == 'help':
            client.help()
        elif command[0] == 'ls':
            client.ls()
        elif command[0] == 'cd..':
            client.cdBack()
        elif command[0] == 'cd':
            client.cd(command[1])
        elif command[0] == 'upload':
            client.upload(command[1])
        elif command[0] == 'download':
            client.download(command[1])
        elif command[0] == 'rm':
            client.rm(command[1])
        elif command[0] == 'mkdir':
            client.mkdir(command[1])
        elif command[0] == 'open':
            client.open(command[1])
        elif command[0] == 'close':
            client.close(command[1])
        elif command[0] == 'create':
            client.create(command[1])


if __name__=="__main__":
    # 执行时输入客户端id: python3 client.py arg_id
    clientId = int(sys.argv[1])
    startClient(clientId)