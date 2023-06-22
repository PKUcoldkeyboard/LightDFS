# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: status_code.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11status_code.proto\x12\x08lightdfs\"g\n\x06Params\x12\x17\n\x0freport_interval\x18\x01 \x01(\x05\x12\x13\n\x0breport_size\x18\x02 \x01(\x05\x12\x14\n\x0crecover_size\x18\x03 \x01(\x05\x12\x19\n\x11keepalive_timeout\x18\x04 \x01(\x05*\xe6\x04\n\nStatusCode\x12\x07\n\x03kOK\x10\x00\x12\n\n\x06kNotOK\x10\x01\x12\x0e\n\nkUnknownCs\x10\x02\x12\x11\n\rkVersionError\x10\x03\x12\x0f\n\x0bkIsFollower\x10\x04\x12\x17\n\x13kInShutdownProgress\x10\x05\x12\x11\n\rkBadParameter\x10\x06\x12\x10\n\x0ckDirNotEmpty\x10\x07\x12\x14\n\x10kTargetDirExists\x10\x08\x12\x0f\n\x0bkFileExists\x10\t\x12\x10\n\x0ckBlockClosed\x10\n\x12\x0f\n\x0bkBlockExist\x10\x0b\x12\r\n\tkReadOnly\x10\x0c\x12\x0f\n\x0bkNsNotFound\x10\r\x12\x0f\n\x0bkCsNotFound\x10\x0e\x12\x11\n\rkNoPermission\x10\x0f\x12\x13\n\x0fkNotEnoughQuota\x10\x10\x12\x17\n\x13kNetworkUnavailable\x10\x11\x12\x0c\n\x08kTimeout\x10\x12\x12\x0f\n\x0bkWriteError\x10\x13\x12\x0e\n\nkReadError\x10\x14\x12\x12\n\x0ekNoEnoughSpace\x10\x15\x12\x1d\n\x19kCsTooMuchUnfinishedWrite\x10\x16\x12\x1b\n\x17kCsTooMuchPendingBuffer\x10\x17\x12\x18\n\x14kGetChunkServerError\x10\x18\x12\x10\n\x0ckUpdateError\x10\x19\x12\x13\n\x0fkSyncMetaFailed\x10\x1a\x12\r\n\tkSafeMode\x10\x1b\x12\x10\n\x0ckServiceStop\x10\x1c\x12\x0e\n\nkDirLocked\x10\x1d\x12\x0e\n\nkDirUnlock\x10\x1e\x12\x14\n\x10kDirLockCleaning\x10\x1f*v\n\x11\x43hunkServerStatus\x12\r\n\tkCsActive\x10\x00\x12\x10\n\x0ckCsWaitClean\x10\x01\x12\x0f\n\x0bkCsCleaning\x10\x02\x12\x0e\n\nkCsOffLine\x10\x03\x12\x0e\n\nkCsStandby\x10\x04\x12\x0f\n\x0bkCsReadonly\x10\x05*\x87\x01\n\rRecoverStatus\x12\x11\n\rkNotInRecover\x10\x00\x12\x0e\n\nkLoRecover\x10\x01\x12\x0e\n\nkHiRecover\x10\x02\x12\n\n\x06kCheck\x10\x03\x12\x0f\n\x0bkIncomplete\x10\x04\x12\t\n\x05kLost\x10\x05\x12\x11\n\rkBlockWriting\x10\x06\x12\x08\n\x04kAny\x10\x07*-\n\nSyncStatus\x12\x0e\n\nkSyncWrite\x10\x00\x12\x0f\n\x0bkSyncDelete\x10\x01*!\n\nRecoverPri\x12\t\n\x05kHigh\x10\x00\x12\x08\n\x04kLow\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'status_code_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATUSCODE._serialized_start=137
  _STATUSCODE._serialized_end=751
  _CHUNKSERVERSTATUS._serialized_start=753
  _CHUNKSERVERSTATUS._serialized_end=871
  _RECOVERSTATUS._serialized_start=874
  _RECOVERSTATUS._serialized_end=1009
  _SYNCSTATUS._serialized_start=1011
  _SYNCSTATUS._serialized_end=1056
  _RECOVERPRI._serialized_start=1058
  _RECOVERPRI._serialized_end=1091
  _PARAMS._serialized_start=31
  _PARAMS._serialized_end=134
# @@protoc_insertion_point(module_scope)
