import json
from typing import Any

from inbound.serializers.base import Serializer


class JSONSerializer(Serializer):
    @staticmethod
    def serialize(data: Any) -> bytes:
        return json.dumps(data).encode()

    @staticmethod
    def deserialize(data: bytes) -> Any:
        return json.loads(data.decode())
