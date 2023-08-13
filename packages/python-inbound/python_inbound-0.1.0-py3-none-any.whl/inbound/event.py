from collections import namedtuple
from datetime import datetime
from typing import Any, Type, TypeVar
from cloudevents.pydantic.event import CloudEvent

EventType = TypeVar("EventType", bound="Event")
BaseEvent = namedtuple("BaseEvent", ["type", "data", "headers"], defaults=[..., ..., {}])

class Event(BaseEvent):
    @classmethod
    def from_cloud_event(cls: Type[EventType], event: CloudEvent | dict) -> EventType:
        if isinstance(event, dict):
            event = CloudEvent.parse_obj(event)

        headers = dict(event.get_attributes())
        return cls(
            type=headers.pop("type"),
            headers=headers,
            data=event.get_data(),
        )

    def to_cloud_event(self) -> CloudEvent:
        return CloudEvent.create({"type": self.type, **self.headers}, self.data)

    @classmethod
    def create(
        cls: Type[EventType],
        type: str,
        data: Any,
        headers: dict[str, str] = {}
    ) -> EventType:
        if not headers.get("time", None):
            headers["time"] = datetime.utcnow().isoformat()

        return cls(type=type, data=data, headers=headers)
