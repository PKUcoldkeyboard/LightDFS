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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10nameserver.proto\x12\x08lightdfs\",\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"8\n\x0e\x44\x61taServerInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"\x12\n\x05\x65mpty\x12\t\n\x01\x65\x18\x01 \x01(\x05\"s\n\x19GetDataServerListResponse\x12\x0f\n\x07success\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x34\n\x12\x64\x61taServerInfoList\x18\x03 \x03(\x0b\x32\x18.lightdfs.DataServerInfo\"5\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"!\n\rLogoutRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"H\n\x0fLockFileRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x11\n\tlock_type\x18\x02 \x01(\x05\x12\x10\n\x08\x66ilepath\x18\x03 \x01(\t\"J\n\x11UnlockFileRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x11\n\tlock_type\x18\x02 \x01(\x05\x12\x10\n\x08\x66ilepath\x18\x03 \x01(\t\"9\n\x11\x43heckCacheRequest\x12\x15\n\rabsolute_path\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\x02\"+\n\x12GetFileInfoRequest\x12\x15\n\rabsolute_path\x18\x01 \x01(\t\"]\n\x08\x46ileInfo\x12\x15\n\rabsolute_path\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x0e\n\x06is_dir\x18\x03 \x01(\x08\x12\r\n\x05\x63time\x18\x04 \x01(\x02\x12\r\n\x05mtime\x18\x05 \x01(\x02\"&\n\rDeleteRequest\x12\x15\n\rabsolute_path\x18\x01 \x01(\t\"j\n\x11ModifyFileRequest\x12\x19\n\x11old_absolute_path\x18\x01 \x01(\t\x12\x19\n\x11new_absolute_path\x18\x02 \x01(\t\x12\x10\n\x08new_size\x18\x03 \x01(\x03\x12\r\n\x05mtime\x18\x04 \x01(\x02\"p\n\x10\x46ileInfoResponse\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0e\n\x06is_dir\x18\x02 \x01(\x08\x12\r\n\x05\x63time\x18\x03 \x01(\x02\x12\r\n\x05mtime\x18\x04 \x01(\x02\x12\x0f\n\x07success\x18\x05 \x01(\x05\x12\x0f\n\x07message\x18\x06 \x01(\t\"4\n\x0fListFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\"G\n\x10ListFileResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0f\n\x07success\x18\x02 \x01(\x05\x12\r\n\x05\x66iles\x18\x03 \x03(\t2\xfc\x06\n\nNameServer\x12\x42\n\x12RegisterDataServer\x12\x18.lightdfs.DataServerInfo\x1a\x12.lightdfs.Response\x12I\n\x11GetDataServerList\x12\x0f.lightdfs.empty\x1a#.lightdfs.GetDataServerListResponse\x12@\n\x10LogoutDataServer\x12\x18.lightdfs.DataServerInfo\x1a\x12.lightdfs.Response\x12=\n\x0cRegisterUser\x12\x19.lightdfs.RegisterRequest\x1a\x12.lightdfs.Response\x12\x33\n\x05Login\x12\x16.lightdfs.LoginRequest\x1a\x12.lightdfs.Response\x12\x35\n\x06Logout\x12\x17.lightdfs.LogoutRequest\x1a\x12.lightdfs.Response\x12\x39\n\x08LockFile\x12\x19.lightdfs.LockFileRequest\x1a\x12.lightdfs.Response\x12=\n\nUnlockFile\x12\x1b.lightdfs.UnlockFileRequest\x1a\x12.lightdfs.Response\x12=\n\nCheckCache\x12\x1b.lightdfs.CheckCacheRequest\x1a\x12.lightdfs.Response\x12\x31\n\x07\x41\x64\x64\x46ile\x12\x12.lightdfs.FileInfo\x1a\x12.lightdfs.Response\x12\x39\n\nDeleteFile\x12\x17.lightdfs.DeleteRequest\x1a\x12.lightdfs.Response\x12=\n\nModifyFile\x12\x1b.lightdfs.ModifyFileRequest\x1a\x12.lightdfs.Response\x12G\n\x0bGetFileInfo\x12\x1c.lightdfs.GetFileInfoRequest\x1a\x1a.lightdfs.FileInfoResponse\x12\x43\n\x08ListFile\x12\x19.lightdfs.ListFileRequest\x1a\x1a.lightdfs.ListFileResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nameserver_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESPONSE._serialized_start=30
  _RESPONSE._serialized_end=74
  _DATASERVERINFO._serialized_start=76
  _DATASERVERINFO._serialized_end=132
  _EMPTY._serialized_start=134
  _EMPTY._serialized_end=152
  _GETDATASERVERLISTRESPONSE._serialized_start=154
  _GETDATASERVERLISTRESPONSE._serialized_end=269
  _REGISTERREQUEST._serialized_start=271
  _REGISTERREQUEST._serialized_end=324
  _LOGINREQUEST._serialized_start=326
  _LOGINREQUEST._serialized_end=376
  _LOGOUTREQUEST._serialized_start=378
  _LOGOUTREQUEST._serialized_end=411
  _LOCKFILEREQUEST._serialized_start=413
  _LOCKFILEREQUEST._serialized_end=485
  _UNLOCKFILEREQUEST._serialized_start=487
  _UNLOCKFILEREQUEST._serialized_end=561
  _CHECKCACHEREQUEST._serialized_start=563
  _CHECKCACHEREQUEST._serialized_end=620
  _GETFILEINFOREQUEST._serialized_start=622
  _GETFILEINFOREQUEST._serialized_end=665
  _FILEINFO._serialized_start=667
  _FILEINFO._serialized_end=760
  _DELETEREQUEST._serialized_start=762
  _DELETEREQUEST._serialized_end=800
  _MODIFYFILEREQUEST._serialized_start=802
  _MODIFYFILEREQUEST._serialized_end=908
  _FILEINFORESPONSE._serialized_start=910
  _FILEINFORESPONSE._serialized_end=1022
  _LISTFILEREQUEST._serialized_start=1024
  _LISTFILEREQUEST._serialized_end=1076
  _LISTFILERESPONSE._serialized_start=1078
  _LISTFILERESPONSE._serialized_end=1149
  _NAMESERVER._serialized_start=1152
  _NAMESERVER._serialized_end=2044
# @@protoc_insertion_point(module_scope)
