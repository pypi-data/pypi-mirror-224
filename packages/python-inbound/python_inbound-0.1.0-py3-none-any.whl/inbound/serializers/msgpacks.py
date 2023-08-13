import msgpack
from typing import Any

from inbound.serializers.base import Serializer


class MsgPackSerializer(Serializer):
    @staticmethod
    def serialize(data: Any) -> bytes:
        return msgpack.packb(data)

    @staticmethod
    def deserialize(data: bytes) -> Any:
        return msgpack.unpackb(data)
