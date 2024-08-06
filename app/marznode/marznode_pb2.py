# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/marznode/marznode.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61pp/marznode/marznode.proto\x12\x08marznode\"\x07\n\x05\x45mpty\"z\n\x07\x42\x61\x63kend\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04type\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07version\x18\x03 \x01(\tH\x01\x88\x01\x01\x12#\n\x08inbounds\x18\x04 \x03(\x0b\x32\x11.marznode.InboundB\x07\n\x05_typeB\n\n\x08_version\"7\n\x10\x42\x61\x63kendsResponse\x12#\n\x08\x62\x61\x63kends\x18\x01 \x03(\x0b\x32\x11.marznode.Backend\"6\n\x07Inbound\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x13\n\x06\x63onfig\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_config\"1\n\x04User\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\"M\n\x08UserData\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.marznode.User\x12#\n\x08inbounds\x18\x02 \x03(\x0b\x32\x11.marznode.Inbound\"3\n\tUsersData\x12&\n\nusers_data\x18\x01 \x03(\x0b\x32\x12.marznode.UserData\"j\n\nUsersStats\x12\x33\n\x0busers_stats\x18\x01 \x03(\x0b\x32\x1e.marznode.UsersStats.UserStats\x1a\'\n\tUserStats\x12\x0b\n\x03uid\x18\x01 \x01(\r\x12\r\n\x05usage\x18\x02 \x01(\x04\"\x17\n\x07LogLine\x12\x0c\n\x04line\x18\x01 \x01(\t\"U\n\rBackendConfig\x12\x15\n\rconfiguration\x18\x01 \x01(\t\x12-\n\rconfig_format\x18\x02 \x01(\x0e\x32\x16.marznode.ConfigFormat\"B\n\x12\x42\x61\x63kendLogsRequest\x12\x14\n\x0c\x62\x61\x63kend_name\x18\x01 \x01(\t\x12\x16\n\x0einclude_buffer\x18\x02 \x01(\x08\"f\n\x15RestartBackendRequest\x12\x14\n\x0c\x62\x61\x63kend_name\x18\x01 \x01(\t\x12,\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.marznode.BackendConfigH\x00\x88\x01\x01\x42\t\n\x07_config\"\x1f\n\x0c\x42\x61\x63kendStats\x12\x0f\n\x07running\x18\x01 \x01(\x08*-\n\x0c\x43onfigFormat\x12\t\n\x05PLAIN\x10\x00\x12\x08\n\x04JSON\x10\x01\x12\x08\n\x04YAML\x10\x02\x32\xfe\x03\n\x0bMarzService\x12\x32\n\tSyncUsers\x12\x12.marznode.UserData\x1a\x0f.marznode.Empty(\x01\x12\x37\n\x0fRepopulateUsers\x12\x13.marznode.UsersData\x1a\x0f.marznode.Empty\x12<\n\rFetchBackends\x12\x0f.marznode.Empty\x1a\x1a.marznode.BackendsResponse\x12\x38\n\x0f\x46\x65tchUsersStats\x12\x0f.marznode.Empty\x1a\x14.marznode.UsersStats\x12@\n\x12\x46\x65tchBackendConfig\x12\x11.marznode.Backend\x1a\x17.marznode.BackendConfig\x12\x42\n\x0eRestartBackend\x12\x1f.marznode.RestartBackendRequest\x1a\x0f.marznode.Empty\x12\x46\n\x11StreamBackendLogs\x12\x1c.marznode.BackendLogsRequest\x1a\x11.marznode.LogLine0\x01\x12<\n\x0fGetBackendStats\x12\x11.marznode.Backend\x1a\x16.marznode.BackendStatsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.marznode.marznode_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONFIGFORMAT']._serialized_start=895
  _globals['_CONFIGFORMAT']._serialized_end=940
  _globals['_EMPTY']._serialized_start=41
  _globals['_EMPTY']._serialized_end=48
  _globals['_BACKEND']._serialized_start=50
  _globals['_BACKEND']._serialized_end=172
  _globals['_BACKENDSRESPONSE']._serialized_start=174
  _globals['_BACKENDSRESPONSE']._serialized_end=229
  _globals['_INBOUND']._serialized_start=231
  _globals['_INBOUND']._serialized_end=285
  _globals['_USER']._serialized_start=287
  _globals['_USER']._serialized_end=336
  _globals['_USERDATA']._serialized_start=338
  _globals['_USERDATA']._serialized_end=415
  _globals['_USERSDATA']._serialized_start=417
  _globals['_USERSDATA']._serialized_end=468
  _globals['_USERSSTATS']._serialized_start=470
  _globals['_USERSSTATS']._serialized_end=576
  _globals['_USERSSTATS_USERSTATS']._serialized_start=537
  _globals['_USERSSTATS_USERSTATS']._serialized_end=576
  _globals['_LOGLINE']._serialized_start=578
  _globals['_LOGLINE']._serialized_end=601
  _globals['_BACKENDCONFIG']._serialized_start=603
  _globals['_BACKENDCONFIG']._serialized_end=688
  _globals['_BACKENDLOGSREQUEST']._serialized_start=690
  _globals['_BACKENDLOGSREQUEST']._serialized_end=756
  _globals['_RESTARTBACKENDREQUEST']._serialized_start=758
  _globals['_RESTARTBACKENDREQUEST']._serialized_end=860
  _globals['_BACKENDSTATS']._serialized_start=862
  _globals['_BACKENDSTATS']._serialized_end=893
  _globals['_MARZSERVICE']._serialized_start=943
  _globals['_MARZSERVICE']._serialized_end=1453
# @@protoc_insertion_point(module_scope)
