# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CurrentWeatherInCityService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!CurrentWeatherInCityService.proto\x12\x05greet\".\n\x1eGetCurrentWeatherInCityRequest\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\"V\n\x1c\x43urrentWeatherInCityResponse\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x13\n\x0btemperature\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t2p\n\x1b\x43urrentWeatherInCityService\x12Q\n\x03Get\x12%.greet.GetCurrentWeatherInCityRequest\x1a#.greet.CurrentWeatherInCityResponseB\x10\xaa\x02\rWeatherOnGrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CurrentWeatherInCityService_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rWeatherOnGrpc'
  _globals['_GETCURRENTWEATHERINCITYREQUEST']._serialized_start=44
  _globals['_GETCURRENTWEATHERINCITYREQUEST']._serialized_end=90
  _globals['_CURRENTWEATHERINCITYRESPONSE']._serialized_start=92
  _globals['_CURRENTWEATHERINCITYRESPONSE']._serialized_end=178
  _globals['_CURRENTWEATHERINCITYSERVICE']._serialized_start=180
  _globals['_CURRENTWEATHERINCITYSERVICE']._serialized_end=292
# @@protoc_insertion_point(module_scope)
