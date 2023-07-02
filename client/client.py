import grpc
import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dataserver'))
import dataserver_pb2 as ds_pb2
import dataserver_pb2_grpc as ds_grpc
from utils.settings import DFS_SETTINGS
from utils.snowflake import getId
from utils.filepath import get_full_path


class Client():
    def __init__(self):
        self.current_dir = '/'
        host = DFS_SETTINGS['DATASERVER']['HOST']
        port = DFS_SETTINGS['DATASERVER']['PORT']
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = ds_grpc.DataServerStub(self.channel)

    def touch(self, path):
        sequence_id = getId()
        response = self.stub.CreateFile(
            ds_pb2.CreateFileRequest(path=path, sequence_id=sequence_id))
        print(json.dumps({
            'success': response.success,
            'message': response.message,
            'sequence_id': response.sequence_id,
        }))

    def ls(self, path):
        sequence_id = getId()
        response = self.stub.ListFile(
            ds_pb2.ListFileRequest(path=path, sequence_id=sequence_id))
        files = response.files
        for file in files:
            print(file, end=' ')
        print()
        
    def mkdir(self, path, parent=False):
        sequence_id = getId()
        response = self.stub.CreateDirectory(
            ds_pb2.CreateDirectoryRequest(path=path, parent=parent, sequence_id=sequence_id))
        print(json.dumps({
            'success': response.success,
            'message': response.message,
            'sequence_id': response.sequence_id,
        }))
        
    def cat(self, path):
        sequence_id = getId()
        response = self.stub.ReadFile(
            ds_pb2.ReadFileRequest(path=path, sequence_id=sequence_id))
        print(response.content, end='')
        
    def rm(self, path, recursive=False):
        sequence_id = getId()
        response = self.stub.DeleteFile(
            ds_pb2.DeleteFileRequest(path=path, recursive=recursive, sequence_id=sequence_id))
        print(json.dumps({
            'success': response.success,
            'message': response.message,
            'sequence_id': response.sequence_id,
        }))


if __name__ == "__main__":
    client = Client()
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
                