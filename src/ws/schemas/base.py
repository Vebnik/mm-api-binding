from pydantic import BaseModel
from typing import Any

from src.bot.schemas import Event
from src.ws.schemas import posts,reaction_added


class BaseEvent(BaseModel):
    event: str
    data: Any
    broadcast: dict
    seq: int


event_model = {
    Event.posted: posts.PostedEvent,
    Event.reaction_added: reaction_added.ReactionAddedEvent
}