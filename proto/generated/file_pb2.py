# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nfile.proto\x12\x08lightdfs\"\xd4\x01\n\x08\x46ileInfo\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0e\n\x06\x62locks\x18\x04 \x03(\x03\x12\r\n\x05\x63time\x18\x05 \x01(\r\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\x03\x12\x10\n\x08replicas\x18\x08 \x01(\x05\x12\x17\n\x0fparent_entry_id\x18\t \x01(\x03\x12\r\n\x05owner\x18\n \x01(\x05\x12\x10\n\x08\x63s_addrs\x18\x0b \x03(\t\x12\x10\n\x08sym_link\x18\x0c \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILEINFO._serialized_start=25
  _FILEINFO._serialized_end=237
# @@protoc_insertion_point(module_scope)
