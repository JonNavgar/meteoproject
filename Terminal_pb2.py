# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Terminal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eTerminal.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"N\n\x0cWellnessData\x12,\n\x08\x64\x61tetime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08wellness\x18\x02 \x01(\x02\"P\n\rPollutionData\x12,\n\x08\x64\x61tetime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tpollution\x18\x02 \x01(\x02\"f\n\x0c\x43ompleteData\x12!\n\x08wellness\x18\x01 \x01(\x0b\x32\r.WellnessDataH\x00\x12#\n\tpollution\x18\x02 \x01(\x0b\x32\x0e.PollutionDataH\x00\x42\x0e\n\x0c\x43ompleteData2C\n\x08Terminal\x12\x37\n\x0csend_results\x12\r.CompleteData\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Terminal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WELLNESSDATA._serialized_start=80
  _WELLNESSDATA._serialized_end=158
  _POLLUTIONDATA._serialized_start=160
  _POLLUTIONDATA._serialized_end=240
  _COMPLETEDATA._serialized_start=242
  _COMPLETEDATA._serialized_end=344
  _TERMINAL._serialized_start=346
  _TERMINAL._serialized_end=413
# @@protoc_insertion_point(module_scope)
