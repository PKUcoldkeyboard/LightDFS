import grpc
import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dataserver'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'nameserver'))
from utils.filepath import get_full_path
from utils.snowflake import getId
from utils.settings import DFS_SETTINGS
import dataserver_pb2_grpc as ds_grpc
import dataserver_pb2 as ds_pb2
import nameserver_pb2_grpc as ns_grpc
import nameserver_pb2 as ns_pb2

class Client():
    def __init__(self):
        self.current_dir = '/'
        ds_host = DFS_SETTINGS['DATASERVER']['HOST']
        ds_port = DFS_SETTINGS['DATASERVER']['PORT']
        ns_host = DFS_SETTINGS['NAMESERVER']['HOST']
        ns_post = DFS_SETTINGS['NAMESERVER']['PORT']
        channel = grpc.insecure_channel(f'{ds_host}:{ds_port}')
        ns_channel = grpc.insecure_channel(f'{ns_host}:{ns_post}')
        self.ds_stub = ds_grpc.DataServerStub(channel)
        self.ns_stub = ns_grpc.NameServerStub(ns_channel)

    def register(self, username, password):
        response = self.nameserver_stub.RegisterUser(
            ds_pb2.RegisterRequest(username=username, password=password)
        )
        return response


    def touch(self, path):
        try:
            sequence_id = getId()
            response = self.ds_stub.CreateFile(
                ds_pb2.CreateFileRequest(path=path, sequence_id=sequence_id))
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Create File')

    def ls(self, path):
        try:
            sequence_id = getId()
            response = self.ns_stub.ListFile(
                ns_pb2.ListFileRequest(path=path, sequence_id=sequence_id))
            files = response.files
            for file in files:
                print(file, end=' ')
            print()
        except grpc.RpcError:
            print('Cannot Connect to NameServer')
        except Exception as e:
            print(e)
            print('Cannot List File')

    def mkdir(self, path, parent=False):
        try:
            sequence_id = getId()
            response = self.ds_stub.CreateDirectory(
                ds_pb2.CreateDirectoryRequest(path=path, parent=parent, sequence_id=sequence_id))
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Create Directory')

    def cat(self, path):
        try:
            sequence_id = getId()
            response = self.ds_stub.ReadFile(
                ds_pb2.ReadFileRequest(path=path, sequence_id=sequence_id))
            print(response.content, end='')
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Read File')

    def rm(self, path, recursive=False):
        try:
            sequence_id = getId()
            response = self.ds_stub.DeleteFile(
                ds_pb2.DeleteFileRequest(path=path, recursive=recursive, sequence_id=sequence_id))
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Delete File')

    def mv(self, src, dst):
        try:
            sequence_id = getId()
            response = self.ds_stub.RenameFile(
                ds_pb2.RenameFileRequest(src=src, dst=dst, sequence_id=sequence_id))
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Rename File')

    def cp(self, src, dst, recursive=False):
        try:
            sequence_id = getId()
            response = self.ds_stub.CopyFile(
                ds_pb2.CopyFileRequest(recursive=recursive, src=src, dst=dst, sequence_id=sequence_id))
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Copy File')


    def download(self, path):
        sequence_id = getId()
        localCache_path = DFS_SETTINGS['CLIENT']['DATA_DIR']
        cacheList = os.listdir(localCache_path)
        if path in cacheList:
            filepath = localCache_path + '/' + path
            localmtime = os.path.getmtime(filepath)
            response = self.nameserver_stub.CheckCache(
                ds_pb2.CheckCacheRequest()
            )


if __name__ == "__main__":
    client = Client()
    USERNAME = ""
    while True:
        print("================welcome==================\n")
        print("键入1选择登陆\n")
        print("键入2选择注册\n")
        print("=========================================\n")
        num = input("please input a num:")
        if  num.isnumeric() == True:
            x = int(num)
            if x == 2:
                uname = input('请输入用户名:')
                passwd = input('请输入密码：')
                response = client.register(uname,passwd)
                print(json.dumps({
                'success': response.success,
                'message': response.message,
            }))
                
                

        else:
            print("[-]输入不符合，请重新输入~")
            continue
    # 命令行交互
    while True:
        command = input(
            f"\033[1;32;40m(ldfs) ~{client.current_dir} \033[m> ").split()
        if len(command) == 0:
            continue
        elif command[0] == 'exit':
            print('bye~')
            break
        elif command[0] == 'ls':
            # 只支持两个参数，ls和path
            if len(command) != 1 and len(command) != 2:
                print("ls: argument number must be 1 or 2")
                continue

            if len(command) == 1:
                # 只有一个ls的情况
                path = client.current_dir
            else:
                path = get_full_path(client.current_dir, command[1])

            client.ls(path)
        elif command[0] == "pwd":
            print(client.current_dir)

        elif command[0] == 'touch':
            if len(command) != 2:
                print("touch: argument number must be 2")
                continue

            path = get_full_path(client.current_dir, command[1])

            client.touch(path)

        elif command[0] == 'mkdir':
            if len(command) == 1:
                print("mkdir: missing operand")
                continue

            if len(command) > 3:
                print("mkdir: too many arguments")
                continue

            if len(command) == 2:
                parent = False
                path = get_full_path(client.current_dir, command[1])
            elif len(command) == 3 and command[1] == '-p':
                parent = True
                path = get_full_path(client.current_dir, command[2])

            client.mkdir(path, parent)

        elif command[0] == 'cat':
            if len(command) == 1:
                print("cat: missing operand")
                continue

            if len(command) > 2:
                print("cat: too many arguments")
                continue

            if len(command) == 2:
                path = get_full_path(client.current_dir, command[1])

            client.cat(path)

        elif command[0] == 'rm':
            if len(command) == 1:
                print("rm: missing operand")
                continue

            if len(command) > 4:
                print("rm: too many arguments")
                continue

            if len(command) == 2:
                path = get_full_path(client.current_dir, command[1])
                client.rm(path)
            elif len(command) == 3 and command[1] == '-r':
                path = get_full_path(client.current_dir, command[2])
                client.rm(path, True)

        elif command[0] == 'mv':
            if len(command) <= 2:
                print("mv: missing operand")
                continue

            if len(command) > 3:
                print("mv: too many arguments")
                continue

            if len(command) == 3:
                src = get_full_path(client.current_dir, command[1])
                dst = get_full_path(client.current_dir, command[2])
                client.mv(src, dst)

        elif command[0] == 'cp':
            if len(command) <= 2:
                print("cp: missing operand")
                continue

            if len(command) > 4:
                print("cp: too many arguments")
                continue

            if len(command) == 3:
                src = get_full_path(client.current_dir, command[1])
                dst = get_full_path(client.current_dir, command[2])
                client.cp(src, dst)
            elif len(command) == 4 and command[1] == '-r':
                src = get_full_path(client.current_dir, command[1])
                dst = get_full_path(client.current_dir, command[2])
                client.cp(src, dst, True)
