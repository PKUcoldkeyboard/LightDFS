# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MetaServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MetaServer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10MetaServer.proto\"2\n\nserverInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"\x16\n\x08serverId\x12\n\n\x02id\x18\x01 \x01(\x05\"\x12\n\x05\x65mpty\x12\t\n\x01\x65\x18\x01 \x01(\x05\".\n\x08lockInfo\x12\x10\n\x08\x63lientId\x18\x01 \x01(\x05\x12\x10\n\x08\x66ilePath\x18\x02 \x01(\t\"\x18\n\x08ma_reply\x12\x0c\n\x04\x64one\x18\x01 \x01(\x08\"\'\n\nserverList\x12\x19\n\x04list\x18\x01 \x03(\x0b\x32\x0b.serverInfo\"\'\n\tlockReply\x12\x0c\n\x04\x64one\x18\x01 \x01(\x08\x12\x0c\n\x04info\x18\x02 \x01(\t2\xd9\x01\n\x10managementServer\x12(\n\x0cserverOnline\x12\x0b.serverInfo\x1a\t.ma_reply\"\x00\x12\'\n\rserverOffline\x12\t.serverId\x1a\t.ma_reply\"\x00\x12&\n\rgetServerList\x12\x06.empty\x1a\x0b.serverList\"\x00\x12#\n\x08lockFile\x12\t.lockInfo\x1a\n.lockReply\"\x00\x12%\n\nunlockFile\x12\t.lockInfo\x1a\n.lockReply\"\x00\x62\x06proto3'
)




_SERVERINFO = _descriptor.Descriptor(
  name='serverInfo',
  full_name='serverInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='serverInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='serverInfo.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='serverInfo.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=70,
)


_SERVERID = _descriptor.Descriptor(
  name='serverId',
  full_name='serverId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='serverId.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=94,
)


_EMPTY = _descriptor.Descriptor(
  name='empty',
  full_name='empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='e', full_name='empty.e', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=114,
)


_LOCKINFO = _descriptor.Descriptor(
  name='lockInfo',
  full_name='lockInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='lockInfo.clientId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filePath', full_name='lockInfo.filePath', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=162,
)


_MA_REPLY = _descriptor.Descriptor(
  name='ma_reply',
  full_name='ma_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='done', full_name='ma_reply.done', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=188,
)


_SERVERLIST = _descriptor.Descriptor(
  name='serverList',
  full_name='serverList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='serverList.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=229,
)


_LOCKREPLY = _descriptor.Descriptor(
  name='lockReply',
  full_name='lockReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='done', full_name='lockReply.done', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='lockReply.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=270,
)

_SERVERLIST.fields_by_name['list'].message_type = _SERVERINFO
DESCRIPTOR.message_types_by_name['serverInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['serverId'] = _SERVERID
DESCRIPTOR.message_types_by_name['empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['lockInfo'] = _LOCKINFO
DESCRIPTOR.message_types_by_name['ma_reply'] = _MA_REPLY
DESCRIPTOR.message_types_by_name['serverList'] = _SERVERLIST
DESCRIPTOR.message_types_by_name['lockReply'] = _LOCKREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

serverInfo = _reflection.GeneratedProtocolMessageType('serverInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFO,
  '__module__' : 'MetaServer_pb2'
  # @@protoc_insertion_point(class_scope:serverInfo)
  })
_sym_db.RegisterMessage(serverInfo)

serverId = _reflection.GeneratedProtocolMessageType('serverId', (_message.Message,), {
  'DESCRIPTOR' : _SERVERID,
  '__module__' : 'MetaServer_pb2'
  # @@protoc_insertion_point(class_scope:serverId)
  })
_sym_db.RegisterMessage(serverId)

empty = _reflection.GeneratedProtocolMessageType('empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'MetaServer_pb2'
  # @@protoc_insertion_point(class_scope:empty)
  })
_sym_db.RegisterMessage(empty)

lockInfo = _reflection.GeneratedProtocolMessageType('lockInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOCKINFO,
  '__module__' : 'MetaServer_pb2'
  # @@protoc_insertion_point(class_scope:lockInfo)
  })
_sym_db.RegisterMessage(lockInfo)

ma_reply = _reflection.GeneratedProtocolMessageType('ma_reply', (_message.Message,), {
  'DESCRIPTOR' : _MA_REPLY,
  '__module__' : 'MetaServer_pb2'
  # @@protoc_insertion_point(class_scope:ma_reply)
  })
_sym_db.RegisterMessage(ma_reply)

serverList = _reflection.GeneratedProtocolMessageType('serverList', (_message.Message,), {
  'DESCRIPTOR' : _SERVERLIST,
  '__module__' : 'MetaServer_pb2'
  # @@protoc_insertion_point(class_scope:serverList)
  })
_sym_db.RegisterMessage(serverList)

lockReply = _reflection.GeneratedProtocolMessageType('lockReply', (_message.Message,), {
  'DESCRIPTOR' : _LOCKREPLY,
  '__module__' : 'MetaServer_pb2'
  # @@protoc_insertion_point(class_scope:lockReply)
  })
_sym_db.RegisterMessage(lockReply)



_MANAGEMENTSERVER = _descriptor.ServiceDescriptor(
  name='managementServer',
  full_name='managementServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=273,
  serialized_end=490,
  methods=[
  _descriptor.MethodDescriptor(
    name='serverOnline',
    full_name='managementServer.serverOnline',
    index=0,
    containing_service=None,
    input_type=_SERVERINFO,
    output_type=_MA_REPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='serverOffline',
    full_name='managementServer.serverOffline',
    index=1,
    containing_service=None,
    input_type=_SERVERID,
    output_type=_MA_REPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getServerList',
    full_name='managementServer.getServerList',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_SERVERLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='lockFile',
    full_name='managementServer.lockFile',
    index=3,
    containing_service=None,
    input_type=_LOCKINFO,
    output_type=_LOCKREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='unlockFile',
    full_name='managementServer.unlockFile',
    index=4,
    containing_service=None,
    input_type=_LOCKINFO,
    output_type=_LOCKREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGEMENTSERVER)

DESCRIPTOR.services_by_name['managementServer'] = _MANAGEMENTSERVER

# @@protoc_insertion_point(module_scope)
