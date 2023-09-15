from pydantic import BaseModel, field_validator

from src.api.service import Posts
from src.api.schemas import PostData, ReactionData


class Reaction(BaseModel):
    user_id: str
    post_id: str
    emoji_name: str
    create_at: int
    update_at: int
    delete_at: int
    remote_id: str | None
    channel_id: str


class Broadcast(BaseModel):
    omit_users: str | None
    user_id: str | None
    channel_id: str | None
    team_id: str | None
    connection_id: str | None
    omit_connection_id: str | None


class ReactionAddedEventData(BaseModel):
    reaction: Reaction | str = ''

    @field_validator('reaction')
    @classmethod
    def validate_reaction(cls, value: str) -> Reaction:
        return Reaction.model_validate_json(value)
    
    
class ReactionAddedEvent(BaseModel):
    event: str
    data: ReactionAddedEventData
    broadcast: Broadcast
    seq: int

    def reply(self, message: str) -> None:
        data = PostData(
            channel_id=self.broadcast.channel_id,
            root_id=self.data.post.id,
            message=message,
        )

        Posts.create(data)

    def add_reaction(self, emoji: str) -> None:
        data = ReactionData(
            user_id='be8139e5fiy9tc7qwknoih5ddw',
            post_id=self.data.post.id,
            emoji_name=emoji
        )
        Posts.add_reaction(data)

