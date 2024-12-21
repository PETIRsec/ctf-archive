import struct

from enum import Enum
from typing import *

class SdpDataType(Enum):
    INTEGER_POSITIVE = 0
    INTEGER_NEGATIVE = 1
    FLOAT = 2
    DOUBLE = 3
    STRING = 4
    LIST = 5
    DICT = 6
    STRUCT_BEGIN = 7
    STRUCT_END = 8

class SdpStruct:
    def __init__(self, data: Dict[int, Any] = None):
        self._data = data or {}

    def __getitem__(self, key: int) -> Any:
        return self._data[key]

    def __setitem__(self, key: int, value: Any) -> None:
        self._data[key] = value

    def __delitem__(self, key: int) -> None:
        del self._data[key]

    def __repr__(self) -> str:
        return f'{self._data}'

    def __eq__(self, other: 'SdpStruct') -> bool:
        return isinstance(other, SdpStruct) and self._data == other._data
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, key):
        return key in self._data
    
    def __json__(self):
        return self._data
    
    def get(self, key, default=None):
        return self._data.get(key, default)

    def items(self):
        return self._data.items()

    @staticmethod
    def _pack_number(value: int) -> bytes:
        result = bytearray()
        while value > 0x7F:
            result.append((value & 0x7F) | 0x80)
            value >>= 7
        result.append(value)
        return bytes(result)

    @classmethod
    def _pack_value(cls, tag: int, value: Any) -> bytes:
        if isinstance(value, int):
            type_ = SdpDataType.INTEGER_POSITIVE if value >= 0 else SdpDataType.INTEGER_NEGATIVE
            header = (type_.value << 4) | (tag if tag < 15 else 15)
            result = bytes([header])
            if tag >= 15:
                result += cls._pack_number(tag)
            result += cls._pack_number(abs(value))
        elif isinstance(value, float):
            type_ = SdpDataType.DOUBLE
            header = (type_.value << 4) | (tag if tag < 15 else 15)
            result = bytes([header])
            if tag >= 15:
                result += cls._pack_number(tag)
            result += struct.pack('d', value)
        elif isinstance(value, str) or isinstance(value, bytes):
            type_ = SdpDataType.STRING
            header = (type_.value << 4) | (tag if tag < 15 else 15)
            result = bytes([header])
            if tag >= 15:
                result += cls._pack_number(tag)
            encoded = value.encode('utf-8') if isinstance(value, str) else value 
            result += cls._pack_number(len(encoded)) + encoded
        elif isinstance(value, list):
            type_ = SdpDataType.LIST
            header = (type_.value << 4) | (tag if tag < 15 else 15)
            result = bytes([header])
            if tag >= 15:
                result += cls._pack_number(tag)
            result += cls._pack_number(len(value))
            for item in value:
                result += cls._pack_value(0, item)
        elif isinstance(value, dict):
            type_ = SdpDataType.DICT
            header = (type_.value << 4) | (tag if tag < 15 else 15)
            result = bytes([header])
            if tag >= 15:
                result += cls._pack_number(tag)
            result += cls._pack_number(len(value))
            for k, v in value.items():
                result += cls._pack_value(0, k)
                result += cls._pack_value(0, v)
        elif isinstance(value, SdpStruct):
            type_ = SdpDataType.STRUCT_BEGIN
            header = (type_.value << 4) | (tag if tag < 15 else 15)
            result = bytes([header])
            if tag >= 15:
                result += cls._pack_number(tag)
            for sub_tag, sub_value in value.items():
                result += cls._pack_value(sub_tag, sub_value)
            result += bytes([SdpDataType.STRUCT_END.value << 4])
        else:
            raise ValueError(f'Unsupported type: {type(value)}')
        return result

    def pack(self) -> bytes:
        result = bytes([SdpDataType.STRUCT_BEGIN.value << 4])
        for tag, value in sorted(self._data.items()):
            result += self._pack_value(tag, value)
        result += bytes([SdpDataType.STRUCT_END.value << 4])
        return result