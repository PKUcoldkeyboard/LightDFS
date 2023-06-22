# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chunkserver.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import status_code_pb2 as status__code__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63hunkserver.proto\x12\x08lightdfs\x1a\x11status_code.proto\"\xfb\x01\n\x11WriteBlockRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x12\n\npacket_seq\x18\x04 \x01(\x05\x12\x0f\n\x07\x64\x61tabuf\x18\x05 \x01(\x0c\x12\x14\n\x0c\x63hunkservers\x18\x06 \x03(\t\x12\x0f\n\x07is_last\x18\x07 \x01(\x08\x12\x0c\n\x04\x64\x65sc\x18\x0b \x03(\t\x12\x11\n\ttimestamp\x18\x0c \x03(\x03\x12\x17\n\x0frecover_version\x18\r \x01(\x05\x12\x15\n\rsync_on_close\x18\x0e \x01(\x08\x12\x12\n\ntotal_size\x18\x0f \x01(\x03\"\xb4\x01\n\x12WriteBlockResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.lightdfs.StatusCode\x12\x17\n\x0f\x62\x61\x64_chunkserver\x18\x03 \x01(\t\x12\x14\n\x0c\x63urrent_size\x18\x04 \x01(\x03\x12\x13\n\x0b\x63urrent_seq\x18\x05 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x0b \x03(\t\x12\x11\n\ttimestamp\x18\x0c \x03(\x03\"[\n\x10ReadBlockRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x10\n\x08read_len\x18\x04 \x01(\x05\"r\n\x11ReadBlockResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.lightdfs.StatusCode\x12\x0f\n\x07\x64\x61tabuf\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\t \x03(\x03\"<\n\x13GetBlockInfoRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x03\"x\n\x14GetBlockInfoResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.lightdfs.StatusCode\x12\x12\n\nblock_size\x18\x03 \x01(\x03\x12\x11\n\ttimestamp\x18\t \x03(\x03\x32\xeb\x01\n\x0b\x43hunkServer\x12G\n\nWriteBlock\x12\x1b.lightdfs.WriteBlockRequest\x1a\x1c.lightdfs.WriteBlockResponse\x12\x44\n\tReadBlock\x12\x1a.lightdfs.ReadBlockRequest\x1a\x1b.lightdfs.ReadBlockResponse\x12M\n\x0cGetBlockInfo\x12\x1d.lightdfs.GetBlockInfoRequest\x1a\x1e.lightdfs.GetBlockInfoResponseB\x03\x80\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chunkserver_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001'
  _WRITEBLOCKREQUEST._serialized_start=51
  _WRITEBLOCKREQUEST._serialized_end=302
  _WRITEBLOCKRESPONSE._serialized_start=305
  _WRITEBLOCKRESPONSE._serialized_end=485
  _READBLOCKREQUEST._serialized_start=487
  _READBLOCKREQUEST._serialized_end=578
  _READBLOCKRESPONSE._serialized_start=580
  _READBLOCKRESPONSE._serialized_end=694
  _GETBLOCKINFOREQUEST._serialized_start=696
  _GETBLOCKINFOREQUEST._serialized_end=756
  _GETBLOCKINFORESPONSE._serialized_start=758
  _GETBLOCKINFORESPONSE._serialized_end=878
  _CHUNKSERVER._serialized_start=881
  _CHUNKSERVER._serialized_end=1116
# @@protoc_insertion_point(module_scope)
