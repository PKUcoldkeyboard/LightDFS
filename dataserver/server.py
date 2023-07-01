import grpc
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import dataserver.dataserver_pb2_grpc as ds_grpc
import dataserver.dataserver_pb2 as ds_pb2
from concurrent import futures
from utils.logger import configure_logger
from utils.settings import DFS_SETTINGS


class DataServicer(ds_grpc.dataserverServicer):
    def __init__(self, host='localhost', port=9001, data_dir='/tmp/lightdfs/dataserver', root='/'):
        self.logger = configure_logger()
        self.host = host
        self.port = port
        self.data_dir = data_dir
        self.root = root
        self.logger.info(f"Data server {self.host} started, port: {self.port}")
        self.logger.info(f"Data server root: {self.root}")

    def mkdir(self, request, context):
        self.logger.info("mkdir %s" % request.path)
        path = f'{self.data_dir}/{self.root}/{request.path}'
        try:
            os.mkdir(path)
        except Exception as e:
            self.logger.error(e)
            return ds_pb2.response(code=0, message=str(e))
        return ds_pb2.response(code=1, message="Create directory successfully! ")


def start_server():
    host = DFS_SETTINGS['DATASERVER']['HOST']
    port = DFS_SETTINGS['DATASERVER']['PORT']
    data_dir = DFS_SETTINGS['DATASERVER']['DATA_DIR']
    root = DFS_SETTINGS['ROOT']
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ds_grpc.add_dataserverServicer_to_server(DataServicer(
        host=host, port=port, data_dir=data_dir, root=root), server)
    server.add_insecure_port('[::]:9000')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    start_server()
