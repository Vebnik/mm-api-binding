from pydantic import BaseModel, field_validator

from src.api.api import Posts
from src.api.schemas import PostData



class Post(BaseModel):
    id: str
    create_at: int
    user_id: str


class Broadcast(BaseModel):
    omit_users: str | None
    user_id: str | None
    channel_id: str | None
    team_id: str | None
    connection_id: str | None
    omit_connection_id: str | None


class PostedEventData(BaseModel):
    channel_display_name: str
    channel_name: str
    channel_type: str
    mentions: str | None = None
    post: Post | str = ''
    sender_name: str
    set_online: bool
    team_id: str

    @field_validator('post')
    @classmethod
    def validate_post(cls, value: str) -> Post:
        return Post.model_validate_json(value)
    
    
class PostedEvent(BaseModel):
    event: str
    data: PostedEventData
    broadcast: Broadcast
    seq: int

    def reply(self, message: str) -> None:
        data = PostData(
            channel_id=self.broadcast.channel_id,
            root_id=self.data.post.id,
            message=message,
        )

        Posts.create(data)

    # def add_reaction(self, emoji: str) -> None:
    #     data = PostData
    #     Posts.add_reaction(data)