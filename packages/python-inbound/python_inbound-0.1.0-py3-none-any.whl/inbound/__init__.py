from importlib.metadata import version
__version__ = version("python-inbound")
del version

from inbound.bus import EventBus as EventBus, create_event_bus as create_event_bus
from inbound.stream import (
    EndOfStream as EndOfStream
)
from inbound.callback import (
    EventCallback as EventCallback,
    CallbackGroup as CallbackGroup
)
from inbound.stream import EventStream as EventStream
from inbound.event import Event as Event


__all__ = (
    "create_event_bus",
    "EventBus",
    "Event",
    "ResponseEvent",
    "EventCallback",
    "CallbackGroup",
    "BaseEvent",
    "EndOfStream",
    "StreamFinished",
    "EventStream",
)
