from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteData(_message.Message):
    __slots__ = ["pollution", "wellness"]
    POLLUTION_FIELD_NUMBER: _ClassVar[int]
    WELLNESS_FIELD_NUMBER: _ClassVar[int]
    pollution: PollutionData
    wellness: WellnessData
    def __init__(self, wellness: _Optional[_Union[WellnessData, _Mapping]] = ..., pollution: _Optional[_Union[PollutionData, _Mapping]] = ...) -> None: ...

class PollutionData(_message.Message):
    __slots__ = ["datetime", "pollution"]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    POLLUTION_FIELD_NUMBER: _ClassVar[int]
    datetime: str
    pollution: float
    def __init__(self, datetime: _Optional[str] = ..., pollution: _Optional[float] = ...) -> None: ...

class WellnessData(_message.Message):
    __slots__ = ["datetime", "wellness"]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    WELLNESS_FIELD_NUMBER: _ClassVar[int]
    datetime: str
    wellness: float
    def __init__(self, datetime: _Optional[str] = ..., wellness: _Optional[float] = ...) -> None: ...
