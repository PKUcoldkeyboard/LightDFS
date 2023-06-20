# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\x12\x08lightdfs\"]\n\x0bVoteRequest\x12\x0c\n\x04term\x18\x02 \x01(\x03\x12\x11\n\tcandidate\x18\x03 \x01(\t\x12\x16\n\x0elast_log_index\x18\x04 \x01(\x03\x12\x15\n\rlast_log_term\x18\x05 \x01(\x03\"2\n\x0cVoteResponse\x12\x0c\n\x04term\x18\x02 \x01(\x03\x12\x14\n\x0cvote_granted\x18\x03 \x01(\x08\"Z\n\x08LogEntry\x12\r\n\x05index\x18\x02 \x01(\x03\x12\x0c\n\x04term\x18\x03 \x01(\x03\x12\x10\n\x08log_data\x18\x04 \x01(\x0c\x12\x1f\n\x04type\x18\x05 \x01(\x0e\x32\x11.lightdfs.LogType\"\x9f\x01\n\x14\x41ppendEntriesRequest\x12\x0c\n\x04term\x18\x02 \x01(\x03\x12\x0e\n\x06leader\x18\x03 \x01(\t\x12\x16\n\x0eprev_log_index\x18\x04 \x01(\x03\x12\x15\n\rprev_log_term\x18\x05 \x01(\x03\x12#\n\x07\x65ntries\x18\x06 \x03(\x0b\x32\x12.lightdfs.LogEntry\x12\x15\n\rleader_commit\x18\x07 \x01(\x03\"6\n\x15\x41ppendEntriesResponse\x12\x0c\n\x04term\x18\x02 \x01(\x03\x12\x0f\n\x07success\x18\x03 \x01(\x08*%\n\x07LogType\x12\x0c\n\x08kUserLog\x10\x00\x12\x0c\n\x08kRaftCmd\x10\x01\x32\x93\x01\n\x08RaftNode\x12\x35\n\x04Vote\x12\x15.lightdfs.VoteRequest\x1a\x16.lightdfs.VoteResponse\x12P\n\rAppendEntries\x12\x1e.lightdfs.AppendEntriesRequest\x1a\x1f.lightdfs.AppendEntriesResponseB\x03\x80\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\200\001\001'
  _LOGTYPE._serialized_start=481
  _LOGTYPE._serialized_end=518
  _VOTEREQUEST._serialized_start=24
  _VOTEREQUEST._serialized_end=117
  _VOTERESPONSE._serialized_start=119
  _VOTERESPONSE._serialized_end=169
  _LOGENTRY._serialized_start=171
  _LOGENTRY._serialized_end=261
  _APPENDENTRIESREQUEST._serialized_start=264
  _APPENDENTRIESREQUEST._serialized_end=423
  _APPENDENTRIESRESPONSE._serialized_start=425
  _APPENDENTRIESRESPONSE._serialized_end=479
  _RAFTNODE._serialized_start=521
  _RAFTNODE._serialized_end=668
# @@protoc_insertion_point(module_scope)