import grpc
import os
import sys
import json
import shutil
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
        self.username = None
        self.jwt = None
        self.cache_path = DFS_SETTINGS['CLIENT']['DATA_DIR']
        ns_host = DFS_SETTINGS['NAMESERVER']['HOST']
        ns_post = DFS_SETTINGS['NAMESERVER']['PORT']
        ns_channel = grpc.insecure_channel(f'{ns_host}:{ns_post}')
        self.ns_stub = ns_grpc.NameServerStub(ns_channel)
        
        os.makedirs(self.cache_path, exist_ok=True)

        # 选择一个DataServer
        try:
            response = self.ns_stub.GetDataServerList(ns_pb2.empty(e=0))
            if not response.success:
                print(response.message)
                exit(1)
            else:
                dataServerInfoList = response.dataServerInfoList
                # 打印在线DataServer
                print('===============================================================')
                print('|{:^62}|'.format('Online DataServer List'))
                print('===============================================================')
                print('|{:^20}|{:^20}|{:^20}|'.format('ID', 'Host', 'Port'))
                print('===============================================================')
                for dataServerInfo in dataServerInfoList:
                    id = dataServerInfo.id
                    host = dataServerInfo.host
                    port = dataServerInfo.port
                    print('|{:^20}|{:^20}|{:^20}|'.format(id, host, port))
                print('===============================================================')
                # 用户选择DataServer
                id = int(input('Please choose a DataServer ID Or Index: '))
                if id < 0:
                    print('Invalid DataServer ID')
                    exit(1)
                elif id < 10:
                    dataServerInfo = dataServerInfoList[id]
                    host = dataServerInfo.host
                    port = dataServerInfo.port
                else:  
                    for dataServerInfo in dataServerInfoList:
                        if dataServerInfo.id == id:
                            host = dataServerInfo.host
                            port = dataServerInfo.port
                            break
                os.system('clear')
                channel = grpc.insecure_channel(f'{host}:{port}')
                self.ds_stub = ds_grpc.DataServerStub(channel)
                print(f'Connect to DataServer {host}:{port} Successfully')

        except grpc.RpcError as e:
            print(e)
            exit(1)
        
        except Exception as e:
            print(e)
            exit(1)

    def register(self, username, password):
        try:
            response = self.ns_stub.RegisterUser(
                ns_pb2.RegisterRequest(username=username, password=password)
            )
            print(json.dumps({
                'success': response.success,
                'message': response.message,
            }))
        except grpc.RpcError:
            print('Cannot Connect to NameServer')
        except Exception:
            print('Cannot Register User')

    def login(self, username, password):
        try:
            response = self.ns_stub.Login(ns_pb2.LoginRequest(
                username=username, password=password))
            self.jwt = response.jwt
            self.username = username

            os.makedirs(self.cache_path + '/' + self.username, exist_ok=True)
            return response.success, response.message
        except grpc.RpcError:
            print('Cannot Connect to NameServer')
        except Exception as e:
            print(e)
            print('Cannot Login')

    def touch(self, path):
        try:
            file_path = self.cache_path + '/' + path
            with open (file_path, 'w') as f:
                f.write('')
            # 获取file_path路径文件的创建时间
            ctime = os.path.getctime(file_path)
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            # response = self.ds_stub.CreateFile(
            #     ds_pb2.CreateFileRequest(path=path, sequence_id=sequence_id, ctime=ctime, mtime=ctime), metadata=metadata)
            # print(json.dumps({
            #     'success': response.success,
            #     'message': response.message,
            #     'sequence_id': response.sequence_id,
            # }))
            response = self.ds_stub.UploadFile(ds_pb2.UploadFileRequest(path=path, sequence_id=sequence_id, content=b''), metadata=metadata)
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,   
            }))

        except grpc.RpcError as e:
            print(e)
            print('Cannot Connect to DataServer')
        except Exception as e:
            print(e)
            print('Cannot Create File')

    def ls(self, path):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.ListFile(
                ds_pb2.ListFileRequest(path=path, sequence_id=sequence_id), metadata=metadata)
            files = response.files
            for file in files:
                print(file, end=' ')
            print()
        except grpc.RpcError:
            print(e)
        except Exception as e:
            print(e)
            print('Cannot List File')

    def mkdir(self, path, parent=False):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.CreateDirectory(
                ds_pb2.CreateDirectoryRequest(path=path, parent=parent, sequence_id=sequence_id), metadata=metadata)
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))

            filepath = self.cache_path + '/' + path
            if parent:
                os.makedirs(filepath, exist_ok=True)
            else:
                os.mkdir(filepath)

        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Create Directory')

    def cat(self, path):
        try:
            filepath = self.cache_path + '/' + path
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    print(f.read(), end='')
            else:
                metadata = (('jwt', self.jwt),)
                sequence_id = getId()
                response = self.ds_stub.ReadFile(
                    ds_pb2.ReadFileRequest(path=path, sequence_id=sequence_id), metadata=metadata)
                print(response.content, end='')
                if response.success:
                    with open(filepath, 'w') as f:
                        f.write(response.content)
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Read File')

    def rm(self, path, recursive=False):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.DeleteFile(
                ds_pb2.DeleteFileRequest(path=path, recursive=recursive, sequence_id=sequence_id), metadata=metadata)
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
            if response.success:
                filepath = get_full_path(
                    self.cache_path + f'/{self.username}/', path)
                if os.path.exists(filepath):
                    if os.path.isdir(filepath):
                        if recursive:
                            shutil.rmtree(filepath)
                        else:
                            os.rmdir(filepath)
                    else:
                        os.remove(filepath)
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except FileNotFoundError:
            pass
        except Exception as e:
            print('Cannot Delete File')

    def mv(self, src, dst):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.RenameFile(
                ds_pb2.RenameFileRequest(src=src, dst=dst, sequence_id=sequence_id), metadata=metadata)
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
            if response.success:
                src_filepath = self.cache_path + '/' + src
                dst_filepath = self.cache_path + '/' + dst
                if os.path.exists(src_filepath):
                    os.rename(src_filepath, dst_filepath)
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Rename File')

    def cp(self, src, dst, recursive=False):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.CopyFile(
                ds_pb2.CopyFileRequest(recursive=recursive, src=src, dst=dst, sequence_id=sequence_id), metadata=metadata)
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
            if response.success:
                src_filepath = self.cache_path + '/' + src
                dst_filepath = self.cache_path + '/' + dst
                if os.path.exists(src_filepath):
                    if os.path.isdir(src_filepath):
                        if recursive:
                            shutil.copytree(src_filepath, dst_filepath)
                        else:
                            shutil.copy(src_filepath, dst_filepath)
                    else:
                        shutil.copy(src_filepath, dst_filepath)
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Copy File')

    def download(self, path):
        try:
            file_path = self.cache_path + '/' + path
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.DownloadFile(ds_pb2.DownloadFileRequest(path=path, sequence_id=sequence_id), metadata=metadata)
            if response.success:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('File Downloaded')
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print(e)
            print('Cannot Download File')
            
    def openfile(self, path):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.OpenFile(
                ds_pb2.OpenFileRequest(path=path, sequence_id=sequence_id), metadata=metadata)
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
        except grpc.RpcError as e:
            print(e)
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Open File')
            
    def closefile(self, path):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.CloseFile(
                ds_pb2.CloseFileRequest(path=path, sequence_id=sequence_id), metadata=metadata)
            print(json.dumps({
                'success': response.success,
                'message': response.message,
                'sequence_id': response.sequence_id,
            }))
        except grpc.RpcError as e:
            print(e)
            print('Cannot Connect to DataServer')
        except Exception as e:
            print('Cannot Close File')
            
    def cd(self, path):
        try:
            metadata = (('jwt', self.jwt),)
            sequence_id = getId()
            response = self.ds_stub.ChangeDir(
                ds_pb2.ChangeDirRequest(path=path, sequence_id=sequence_id), metadata=metadata)
            if response.success:
                # 找到path第二个/后的所有路径
                index = path.find('/', 1)
                self.current_dir = path[index:]
        except grpc.RpcError:
            print('Cannot Connect to DataServer')
        except Exception as e:
            print(e)
            print('Cannot Change Directory')


if __name__ == "__main__":
    client = Client()
    while True:
        print("\n=========================================")
        print("|               WELCOME                |")
        print("=========================================")
        print("| 1. Login                             |")
        print("| 2. Register                          |")
        print("| 3. Exit                              |")
        print("=========================================\n")

        num = input("Please enter a number: ")

        if num.isnumeric():
            x = int(num)

            if x == 2:
                uname = input('Please enter your username: ')
                passwd = input('Please enter your password: ')
                client.register(uname, passwd)

            elif x == 1:
                uname = input('Please enter your username: ')
                passwd = input('Please enter your password: ')
                success, msg = client.login(uname, passwd)
                if success:
                    os.system('clear')
                    break
                else:
                    print(f"[-] Login failed, {msg} please try again!")
                    continue

            elif x == 3:
                print("bye~")
                break
            else:
                print("[-] Invalid input, please try again!")
                continue

        else:
            print("[-] Invalid input, please try again!")
            continue

    # 命令行交互
    while True:
        command = input(
            f"\033[1;32;40m(ldfs) ~{client.username} {client.current_dir} \033[m> ").split()
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
                path = f'/{client.username}' + client.current_dir
            else:
                path = get_full_path(f'{client.username}/' + client.current_dir, command[1])

            client.ls(path)
        elif command[0] == "pwd":
            print(client.current_dir)

        elif command[0] == 'touch':
            if len(command) != 2:
                print("touch: argument number must be 2")
                continue

            path = get_full_path(f'/{client.username}' + client.current_dir, command[1])

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
                path = get_full_path(f'/{client.username}' + client.current_dir, command[1])
            elif len(command) == 3 and command[1] == '-p':
                parent = True
                path = get_full_path(f'/{client.username}' + client.current_dir, command[2])

            client.mkdir(path, parent)

        elif command[0] == 'cat':
            if len(command) == 1:
                print("cat: missing operand")
                continue

            if len(command) > 2:
                print("cat: too many arguments")
                continue

            if len(command) == 2:
                path = get_full_path(f'/{client.username}' + client.current_dir, command[1])

            client.cat(path)

        elif command[0] == 'rm':
            if len(command) == 1:
                print("rm: missing operand")
                continue

            if len(command) > 4:
                print("rm: too many arguments")
                continue

            if len(command) == 2:
                path = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                client.rm(path)
            elif len(command) == 3 and command[1] == '-r':
                path = get_full_path(f'/{client.username}' + client.current_dir, command[2])
                client.rm(path, True)

        elif command[0] == 'mv':
            if len(command) <= 2:
                print("mv: missing operand")
                continue

            if len(command) > 3:
                print("mv: too many arguments")
                continue

            if len(command) == 3:
                src = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                dst = get_full_path(f'/{client.username}' + client.current_dir, command[2])
                client.mv(src, dst)

        elif command[0] == 'cp':
            if len(command) <= 2:
                print("cp: missing operand")
                continue

            if len(command) > 4:
                print("cp: too many arguments")
                continue

            if len(command) == 3:
                src = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                dst = get_full_path(f'/{client.username}' + client.current_dir, command[2])
                client.cp(src, dst)
            elif len(command) == 4 and command[1] == '-r':
                src = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                dst = get_full_path(f'/{client.username}' + client.current_dir, command[2])
                client.cp(src, dst, True)

        elif command[0] == 'download':
            if len(command) <= 1:
                print("cp: missing operand")
                continue

            if len(command) > 2:
                print("cp: too many arguments")
                continue

            if len(command) == 2:
                path = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                client.download(path)
        elif command[0] == 'cd':
            if len(command) <= 1:
                print("cd: missing operand")
                continue

            if len(command) > 2:
                print("cd: too many arguments")
                continue

            if len(command) == 2:
                if command[1] == '..' and client.current_dir == '/':
                    continue
                elif command[1] == '..':
                    client.current_dir = os.path.dirname(client.current_dir)
                    continue
                path = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                client.cd(path)
        elif command[0] == 'open':
            if len(command) <= 1:
                print("open: missing operand")
                continue

            if len(command) > 2:
                print("open: too many arguments")
                continue

            if len(command) == 2:
                path = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                client.openfile(path)
        
        elif command[0] == 'close':
            if len(command) <= 1:
                print("close: missing operand")
                continue

            if len(command) > 2:
                print("close: too many arguments")
                continue

            if len(command) == 2:
                path = get_full_path(f'/{client.username}' + client.current_dir, command[1])
                client.closefile(path)
                
        elif command[0] == 'help':
            print("ls: list files in the directory")
            print("pwd: print current directory")
            print("touch: create a new file")
            print("mkdir: create a new directory")
            print("cat: print the content of a file")
            print("rm: remove a file or directory")
            print("mv: move a file or directory")
            print("cp: copy a file or directory")
            print("download: download a file from the server")
            print("cd: change directory")
            print("help: print this help message")
            print("exit: exit the client")
            print("open: open a file in the default application")
            print("clos: close a file in the default application")