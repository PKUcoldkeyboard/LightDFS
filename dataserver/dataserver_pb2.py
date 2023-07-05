# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataserver.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x61taserver.proto\x12\x08lightdfs\"E\n\x0c\x42\x61seResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0f\n\x07success\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\"6\n\x11\x43reateFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\"4\n\x0fListFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\"G\n\x10ListFileResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0f\n\x07success\x18\x02 \x01(\x05\x12\r\n\x05\x66iles\x18\x03 \x03(\t\"K\n\x16\x43reateDirectoryRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06parent\x18\x04 \x01(\x08\"I\n\x11\x44\x65leteFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x11\n\trecursive\x18\x03 \x01(\x08\"B\n\x11RenameFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\x0b\n\x03\x64st\x18\x03 \x01(\t\"4\n\x0fReadFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\"I\n\x10ReadFileResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0f\n\x07success\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"G\n\x11UploadFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"8\n\x13\x44ownloadFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0c\n\x04path\x18\x02 \x01(\t\"M\n\x14\x44ownloadFileResponse\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0f\n\x07success\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"S\n\x0f\x43opyFileRequest\x12\x13\n\x0bsequence_id\x18\x01 \x01(\x03\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\x0b\n\x03\x64st\x18\x03 \x01(\t\x12\x11\n\trecursive\x18\x04 \x01(\x08\x32\x8f\x05\n\nDataServer\x12\x43\n\nCreateFile\x12\x1b.lightdfs.CreateFileRequest\x1a\x16.lightdfs.BaseResponse\"\x00\x12\x43\n\x08ListFile\x12\x19.lightdfs.ListFileRequest\x1a\x1a.lightdfs.ListFileResponse\"\x00\x12M\n\x0f\x43reateDirectory\x12 .lightdfs.CreateDirectoryRequest\x1a\x16.lightdfs.BaseResponse\"\x00\x12\x43\n\nDeleteFile\x12\x1b.lightdfs.DeleteFileRequest\x1a\x16.lightdfs.BaseResponse\"\x00\x12\x43\n\nRenameFile\x12\x1b.lightdfs.RenameFileRequest\x1a\x16.lightdfs.BaseResponse\"\x00\x12\x43\n\x08ReadFile\x12\x19.lightdfs.ReadFileRequest\x1a\x1a.lightdfs.ReadFileResponse\"\x00\x12\x45\n\nUploadFile\x12\x1b.lightdfs.UploadFileRequest\x1a\x16.lightdfs.BaseResponse\"\x00(\x01\x12Q\n\x0c\x44ownloadFile\x12\x1d.lightdfs.DownloadFileRequest\x1a\x1e.lightdfs.DownloadFileResponse\"\x00\x30\x01\x12?\n\x08\x43opyFile\x12\x19.lightdfs.CopyFileRequest\x1a\x16.lightdfs.BaseResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataserver_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BASERESPONSE._serialized_start=30
  _BASERESPONSE._serialized_end=99
  _CREATEFILEREQUEST._serialized_start=101
  _CREATEFILEREQUEST._serialized_end=155
  _LISTFILEREQUEST._serialized_start=157
  _LISTFILEREQUEST._serialized_end=209
  _LISTFILERESPONSE._serialized_start=211
  _LISTFILERESPONSE._serialized_end=282
  _CREATEDIRECTORYREQUEST._serialized_start=284
  _CREATEDIRECTORYREQUEST._serialized_end=359
  _DELETEFILEREQUEST._serialized_start=361
  _DELETEFILEREQUEST._serialized_end=434
  _RENAMEFILEREQUEST._serialized_start=436
  _RENAMEFILEREQUEST._serialized_end=502
  _READFILEREQUEST._serialized_start=504
  _READFILEREQUEST._serialized_end=556
  _READFILERESPONSE._serialized_start=558
  _READFILERESPONSE._serialized_end=631
  _UPLOADFILEREQUEST._serialized_start=633
  _UPLOADFILEREQUEST._serialized_end=704
  _DOWNLOADFILEREQUEST._serialized_start=706
  _DOWNLOADFILEREQUEST._serialized_end=762
  _DOWNLOADFILERESPONSE._serialized_start=764
  _DOWNLOADFILERESPONSE._serialized_end=841
  _COPYFILEREQUEST._serialized_start=843
  _COPYFILEREQUEST._serialized_end=926
  _DATASERVER._serialized_start=929
  _DATASERVER._serialized_end=1584
# @@protoc_insertion_point(module_scope)
