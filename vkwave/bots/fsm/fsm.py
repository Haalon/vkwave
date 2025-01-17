import typing
from enum import Enum, auto

from vkwave.bots import BotType
from vkwave.bots.core.dispatching.events.base import BaseEvent
from vkwave.bots.fsm.types import StateId
from vkwave.bots.storage.base import AbstractStorage
from vkwave.bots.storage.storages import Storage
from vkwave.bots.storage.types import Key, Value


class ForWhat(Enum):
    FOR_CHAT = auto()
    FOR_USER = auto()
    FOR_USER_IN_CHAT = auto()  # default


def get_peer_from_ids(event: BaseEvent) -> typing.Tuple[int, int]:
    if event.bot_type is BotType.BOT:
        if event.object.object.dict().get("message") is not None:
            from_id = event.object.object.message.from_id
            peer_id = event.object.object.message.peer_id
        else:
            # CallbackButtonEventObject
            from_id = event.object.object.user_id
            peer_id = event.object.object.peer_id
    else:
        peer_id = from_id = event.object.object.peer_id
        if peer_id > 2e9:
            from_id = int(event.object.object.message_data.from_id)
    return from_id, peer_id


def create_state_id(event: BaseEvent, for_what: ForWhat = ForWhat.FOR_USER_IN_CHAT) -> StateId:
    res: str

    template = "__vkwave_{for_what}_{peer_id}_{from_id}__"
    from_id, peer_id = get_peer_from_ids(event)

    is_pm = from_id == peer_id
    is_chat = not is_pm
    if for_what is ForWhat.FOR_CHAT:
        if not is_chat:
            raise ValueError("it's not a chat")
        res = template.format(for_what="chat", peer_id=peer_id, from_id=peer_id)
    elif for_what is ForWhat.FOR_USER:
        if not is_pm:
            raise ValueError("it's not a pm")
        res = template.format(for_what="user", peer_id=from_id, from_id=from_id)
    else:
        if not is_chat:
            raise ValueError("it's not a chat")
        res = template.format(for_what="userInChat", peer_id=peer_id, from_id=from_id)

    return StateId(res)


class State:
    def __init__(self, title: str):
        self.title = title


class FiniteStateMachine:
    def __init__(self, storage: typing.Optional[AbstractStorage] = None):
        self.storage = storage or Storage()

    async def set_state(
        self,
        state: State,
        event: BaseEvent,
        for_what: ForWhat,
        extra_state_data: typing.Optional[typing.Dict[str, str]] = None,
    ) -> None:
        sid = Key(create_state_id(event, for_what))
        if extra_state_data is None:
            extra_state_data = {}

        if await self.storage.contains(sid):
            current_data = await self.storage.get(sid)
            current_data["__vkwave_fsm_state__"] = str(state)
            current_data.update(extra_state_data)
            return await self.storage.put(sid, current_data)

        storage_data = {"__vkwave_fsm_state__": str(state)}
        storage_data.update(extra_state_data)
        return await self.storage.put(sid, storage_data)

    async def add_data(
        self, event: BaseEvent, for_what: ForWhat, state_data: typing.Dict[str, str]
    ) -> None:
        sid = Key(create_state_id(event, for_what))

        data = await self.storage.get(sid)
        data.update(state_data)
        return await self.storage.put(sid, data)

    async def get_data(self, event: BaseEvent, for_what: ForWhat) -> typing.Optional[Value]:
        sid = Key(create_state_id(event, for_what))
        return await self.storage.get(sid, default=None)

    async def finish(self, event: BaseEvent, for_what: ForWhat) -> None:
        sid = Key(create_state_id(event, for_what))
        return await self.storage.delete(sid)
