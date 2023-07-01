# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nameserver.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10nameserver.proto\x12\x08lightdfs\"%\n\x08response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"8\n\x0e\x64\x61taServerInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"\x12\n\x05\x65mpty\x12\t\n\x01\x65\x18\x01 \x01(\x05\"l\n\x19getDataServerListResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x34\n\x12\x64\x61taServerInfoList\x18\x03 \x03(\x0b\x32\x18.lightdfs.dataServerInfo\"D\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"a\n\x18setFilePermissionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\x12\x12\n\npermission\x18\x04 \x01(\x05\"5\n\x0flockFileRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t\"7\n\x11unlockFileRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t2\x98\x04\n\nnameserver\x12\x42\n\x12registerDataServer\x12\x18.lightdfs.dataServerInfo\x1a\x12.lightdfs.response\x12I\n\x11getDataServerList\x12\x0f.lightdfs.empty\x1a#.lightdfs.getDataServerListResponse\x12@\n\x10logoutDataServer\x12\x18.lightdfs.dataServerInfo\x1a\x12.lightdfs.response\x12=\n\x0cregisterUser\x12\x19.lightdfs.RegisterRequest\x1a\x12.lightdfs.response\x12\x33\n\x05login\x12\x16.lightdfs.LoginRequest\x1a\x12.lightdfs.response\x12K\n\x11setFilePermission\x12\".lightdfs.setFilePermissionRequest\x1a\x12.lightdfs.response\x12\x39\n\x08lockFile\x12\x19.lightdfs.lockFileRequest\x1a\x12.lightdfs.response\x12=\n\nunlockFile\x12\x1b.lightdfs.unlockFileRequest\x1a\x12.lightdfs.responseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nameserver_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESPONSE._serialized_start=30
  _RESPONSE._serialized_end=67
  _DATASERVERINFO._serialized_start=69
  _DATASERVERINFO._serialized_end=125
  _EMPTY._serialized_start=127
  _EMPTY._serialized_end=145
  _GETDATASERVERLISTRESPONSE._serialized_start=147
  _GETDATASERVERLISTRESPONSE._serialized_end=255
  _REGISTERREQUEST._serialized_start=257
  _REGISTERREQUEST._serialized_end=325
  _LOGINREQUEST._serialized_start=327
  _LOGINREQUEST._serialized_end=377
  _SETFILEPERMISSIONREQUEST._serialized_start=379
  _SETFILEPERMISSIONREQUEST._serialized_end=476
  _LOCKFILEREQUEST._serialized_start=478
  _LOCKFILEREQUEST._serialized_end=531
  _UNLOCKFILEREQUEST._serialized_start=533
  _UNLOCKFILEREQUEST._serialized_end=588
  _NAMESERVER._serialized_start=591
  _NAMESERVER._serialized_end=1127
# @@protoc_insertion_point(module_scope)
