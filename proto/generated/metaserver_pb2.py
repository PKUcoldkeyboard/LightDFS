# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metaserver.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import status_code_pb2 as status__code__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10metaserver.proto\x12\x13lightdfs.metaserver\x1a\x11status_code.proto\"Q\n\x0f\x41\x64\x64\x42lockRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x16\n\x0e\x63lient_address\x18\x03 \x01(\t\"M\n\x10\x41\x64\x64\x42lockResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.lightdfs.StatusCode\"Z\n\x10SyncBlockRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x03\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x03\"N\n\x11SyncBlockResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.lightdfs.StatusCode\"\x93\x01\n\x12\x46inishBlockRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x03\x12\x15\n\rblock_version\x18\x03 \x01(\x03\x12\x11\n\tfile_name\x18\x04 \x01(\t\x12\x12\n\nblock_size\x18\x05 \x01(\x03\x12\x18\n\x10\x63lose_with_error\x18\x06 \x01(\x08\"P\n\x13\x46inishBlockResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.lightdfs.StatusCode\";\n\x12RemoveBlockRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x03\"P\n\x13RemoveBlockResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.lightdfs.StatusCode2\x85\x03\n\nMetaServer\x12W\n\x08\x41\x64\x64\x42lock\x12$.lightdfs.metaserver.AddBlockRequest\x1a%.lightdfs.metaserver.AddBlockResponse\x12Z\n\tSyncBlock\x12%.lightdfs.metaserver.SyncBlockRequest\x1a&.lightdfs.metaserver.SyncBlockResponse\x12`\n\x0b\x46inishBlock\x12\'.lightdfs.metaserver.FinishBlockRequest\x1a(.lightdfs.metaserver.FinishBlockResponse\x12`\n\x0bRemoveBlock\x12\'.lightdfs.metaserver.RemoveBlockRequest\x1a(.lightdfs.metaserver.RemoveBlockResponseB\x03\x80\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metaserver_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001'
  _ADDBLOCKREQUEST._serialized_start=60
  _ADDBLOCKREQUEST._serialized_end=141
  _ADDBLOCKRESPONSE._serialized_start=143
  _ADDBLOCKRESPONSE._serialized_end=220
  _SYNCBLOCKREQUEST._serialized_start=222
  _SYNCBLOCKREQUEST._serialized_end=312
  _SYNCBLOCKRESPONSE._serialized_start=314
  _SYNCBLOCKRESPONSE._serialized_end=392
  _FINISHBLOCKREQUEST._serialized_start=395
  _FINISHBLOCKREQUEST._serialized_end=542
  _FINISHBLOCKRESPONSE._serialized_start=544
  _FINISHBLOCKRESPONSE._serialized_end=624
  _REMOVEBLOCKREQUEST._serialized_start=626
  _REMOVEBLOCKREQUEST._serialized_end=685
  _REMOVEBLOCKRESPONSE._serialized_start=687
  _REMOVEBLOCKRESPONSE._serialized_end=767
  _METASERVER._serialized_start=770
  _METASERVER._serialized_end=1159
# @@protoc_insertion_point(module_scope)
