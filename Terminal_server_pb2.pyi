from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteData(_message.Message):
    __slots__ = ["datetimep", "datetimew", "pollution", "wellness"]
    DATETIMEP_FIELD_NUMBER: _ClassVar[int]
    DATETIMEW_FIELD_NUMBER: _ClassVar[int]
    POLLUTION_FIELD_NUMBER: _ClassVar[int]
    WELLNESS_FIELD_NUMBER: _ClassVar[int]
    datetimep: str
    datetimew: str
    pollution: float
    wellness: float
    def __init__(self, wellness: _Optional[float] = ..., pollution: _Optional[float] = ..., datetimew: _Optional[str] = ..., datetimep: _Optional[str] = ...) -> None: ...
