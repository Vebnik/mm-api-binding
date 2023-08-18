from pydantic import BaseModel
from typing import Any

from src.bot.schemas import Event


class Broadcast(BaseModel):
    omit_users: str|None
    user_id: str
    channel_id: str
    team_id: str
    connection_id: str
    omit_connection_id: str


#
class StatusChangeEventData(BaseModel):
    status: str
    user_id: str

class StatusChangeEvent(BaseModel):
    event: str
    data: StatusChangeEventData
    broadcast: dict
    seq: int
#


#
class HelloEventData(BaseModel):
    connection_id: str
    server_version: str

class HelloEvent(BaseModel):
    event: str
    data: HelloEventData
    broadcast: dict
    seq: int
#


#
class PostedEventData(BaseModel):
    channel_display_name: str
    channel_name: str
    channel_type: str
    mentions: str
    post: str
    sender_name: str
    set_online: bool
    team_id: str

class PostedEvent(BaseModel):
    event: str
    data: PostedEventData
    broadcast: dict
    seq: int
#


event_model = {
    Event.hello: HelloEvent,
    Event.status_change: StatusChangeEvent,
    Event.posted: PostedEvent,
}
    