# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import DataServer_pb2 as DataServer__pb2


class storageServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.synUpload = channel.stream_unary(
                '/storageServer/synUpload',
                request_serializer=DataServer__pb2.upload_file.SerializeToString,
                response_deserializer=DataServer__pb2.reply.FromString,
                )
        self.upload = channel.stream_unary(
                '/storageServer/upload',
                request_serializer=DataServer__pb2.upload_file.SerializeToString,
                response_deserializer=DataServer__pb2.reply.FromString,
                )
        self.download = channel.unary_stream(
                '/storageServer/download',
                request_serializer=DataServer__pb2.file_path.SerializeToString,
                response_deserializer=DataServer__pb2.fileStream.FromString,
                )
        self.ls = channel.unary_unary(
                '/storageServer/ls',
                request_serializer=DataServer__pb2.file_path.SerializeToString,
                response_deserializer=DataServer__pb2.fileList.FromString,
                )
        self.mkdir = channel.unary_unary(
                '/storageServer/mkdir',
                request_serializer=DataServer__pb2.file_path.SerializeToString,
                response_deserializer=DataServer__pb2.reply.FromString,
                )
        self.synDelete = channel.unary_unary(
                '/storageServer/synDelete',
                request_serializer=DataServer__pb2.file_path.SerializeToString,
                response_deserializer=DataServer__pb2.reply.FromString,
                )
        self.delete = channel.unary_unary(
                '/storageServer/delete',
                request_serializer=DataServer__pb2.file_path.SerializeToString,
                response_deserializer=DataServer__pb2.reply.FromString,
                )


class storageServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def synUpload(self, request_iterator, context):
        """上传文件到服务器并同步
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upload(self, request_iterator, context):
        """上传文件到服务器
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def download(self, request, context):
        """从服务器下载文件
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ls(self, request, context):
        """查询目录
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mkdir(self, request, context):
        """创建文件夹
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def synDelete(self, request, context):
        """删除文件并同步
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """删除文件
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_storageServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'synUpload': grpc.stream_unary_rpc_method_handler(
                    servicer.synUpload,
                    request_deserializer=DataServer__pb2.upload_file.FromString,
                    response_serializer=DataServer__pb2.reply.SerializeToString,
            ),
            'upload': grpc.stream_unary_rpc_method_handler(
                    servicer.upload,
                    request_deserializer=DataServer__pb2.upload_file.FromString,
                    response_serializer=DataServer__pb2.reply.SerializeToString,
            ),
            'download': grpc.unary_stream_rpc_method_handler(
                    servicer.download,
                    request_deserializer=DataServer__pb2.file_path.FromString,
                    response_serializer=DataServer__pb2.fileStream.SerializeToString,
            ),
            'ls': grpc.unary_unary_rpc_method_handler(
                    servicer.ls,
                    request_deserializer=DataServer__pb2.file_path.FromString,
                    response_serializer=DataServer__pb2.fileList.SerializeToString,
            ),
            'mkdir': grpc.unary_unary_rpc_method_handler(
                    servicer.mkdir,
                    request_deserializer=DataServer__pb2.file_path.FromString,
                    response_serializer=DataServer__pb2.reply.SerializeToString,
            ),
            'synDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.synDelete,
                    request_deserializer=DataServer__pb2.file_path.FromString,
                    response_serializer=DataServer__pb2.reply.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=DataServer__pb2.file_path.FromString,
                    response_serializer=DataServer__pb2.reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'storageServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class storageServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def synUpload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/storageServer/synUpload',
            DataServer__pb2.upload_file.SerializeToString,
            DataServer__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/storageServer/upload',
            DataServer__pb2.upload_file.SerializeToString,
            DataServer__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/storageServer/download',
            DataServer__pb2.file_path.SerializeToString,
            DataServer__pb2.fileStream.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ls(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storageServer/ls',
            DataServer__pb2.file_path.SerializeToString,
            DataServer__pb2.fileList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mkdir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storageServer/mkdir',
            DataServer__pb2.file_path.SerializeToString,
            DataServer__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def synDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storageServer/synDelete',
            DataServer__pb2.file_path.SerializeToString,
            DataServer__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storageServer/delete',
            DataServer__pb2.file_path.SerializeToString,
            DataServer__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
