# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fault_detector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..model import model_pb2 as model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x66\x61ult_detector.proto\x12\x02v1\x1a\x0bmodel.proto\"E\n\rFaultDetector\x12\"\n\x05rules\x18\x01 \x03(\x0b\x32\x13.v1.FaultDetectRule\x12\x10\n\x08revision\x18\x02 \x01(\t\"\xbd\x04\n\x0f\x46\x61ultDetectRule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x10\n\x08revision\x18\x04 \x01(\t\x12\r\n\x05\x63time\x18\x05 \x01(\t\x12\r\n\x05mtime\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12>\n\x0etarget_service\x18\x15 \x01(\x0b\x32&.v1.FaultDetectRule.DestinationService\x12\x10\n\x08interval\x18\x16 \x01(\r\x12\x0f\n\x07timeout\x18\x17 \x01(\r\x12\x0c\n\x04port\x18\x18 \x01(\r\x12.\n\x08protocol\x18\x19 \x01(\x0e\x32\x1c.v1.FaultDetectRule.Protocol\x12+\n\x0bhttp_config\x18\x1a \x01(\x0b\x32\x16.v1.HttpProtocolConfig\x12)\n\ntcp_config\x18\x1b \x01(\x0b\x32\x15.v1.TcpProtocolConfig\x12)\n\nudp_config\x18\x1c \x01(\x0b\x32\x15.v1.UdpProtocolConfig\x1aY\n\x12\x44\x65stinationService\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x1f\n\x06method\x18\x03 \x01(\x0b\x32\x0f.v1.MatchString\"3\n\x08Protocol\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\x07\n\x03TCP\x10\x02\x12\x07\n\x03UDP\x10\x03J\x04\x08\x08\x10\x15\"\xa3\x01\n\x12HttpProtocolConfig\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x35\n\x07headers\x18\x03 \x03(\x0b\x32$.v1.HttpProtocolConfig.MessageHeader\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x1a+\n\rMessageHeader\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"2\n\x11TcpProtocolConfig\x12\x0c\n\x04send\x18\x01 \x01(\t\x12\x0f\n\x07receive\x18\x02 \x03(\t\"2\n\x11UdpProtocolConfig\x12\x0c\n\x04send\x18\x01 \x01(\t\x12\x0f\n\x07receive\x18\x02 \x03(\tB\x95\x01\n8com.tencent.polaris.specification.api.v1.fault.toleranceB\x12\x46\x61ultDetectorProtoZEgithub.com/polarismesh/specification/source/go/api/v1/fault_toleranceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fault_detector_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n8com.tencent.polaris.specification.api.v1.fault.toleranceB\022FaultDetectorProtoZEgithub.com/polarismesh/specification/source/go/api/v1/fault_tolerance'
  _globals['_FAULTDETECTOR']._serialized_start=41
  _globals['_FAULTDETECTOR']._serialized_end=110
  _globals['_FAULTDETECTRULE']._serialized_start=113
  _globals['_FAULTDETECTRULE']._serialized_end=686
  _globals['_FAULTDETECTRULE_DESTINATIONSERVICE']._serialized_start=538
  _globals['_FAULTDETECTRULE_DESTINATIONSERVICE']._serialized_end=627
  _globals['_FAULTDETECTRULE_PROTOCOL']._serialized_start=629
  _globals['_FAULTDETECTRULE_PROTOCOL']._serialized_end=680
  _globals['_HTTPPROTOCOLCONFIG']._serialized_start=689
  _globals['_HTTPPROTOCOLCONFIG']._serialized_end=852
  _globals['_HTTPPROTOCOLCONFIG_MESSAGEHEADER']._serialized_start=809
  _globals['_HTTPPROTOCOLCONFIG_MESSAGEHEADER']._serialized_end=852
  _globals['_TCPPROTOCOLCONFIG']._serialized_start=854
  _globals['_TCPPROTOCOLCONFIG']._serialized_end=904
  _globals['_UDPPROTOCOLCONFIG']._serialized_start=906
  _globals['_UDPPROTOCOLCONFIG']._serialized_end=956
# @@protoc_insertion_point(module_scope)
