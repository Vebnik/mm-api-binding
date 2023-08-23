from pydantic import BaseModel, field_validator
from src.api.schemas.schemas import PostData
from src.api.schemas.get_post_response import GetPostResponse
from src.api.api import Posts


class Reaction(BaseModel):
    user_id: str
    post_id: str
    emoji_name: str
    channel_id: str


class Broadcast(BaseModel):
    omit_users: str | None
    user_id: str | None
    channel_id: str | None
    team_id: str | None
    connection_id: str | None
    omit_connection_id: str | None


class ReactionAddedEventData(BaseModel):
    reaction: Reaction | str

    @field_validator('reaction')
    @classmethod
    def validate_reaction(cls, value: str) -> Reaction:
        return Reaction.model_validate_json(value)


class ReactionAddedEvent(BaseModel):
    event: str
    data: ReactionAddedEventData
    broadcast: Broadcast
    seq: int

    def reply(self, message: str, root_id: str) -> None:
        data = PostData(
            channel_id=self.broadcast.channel_id,
            root_id=root_id,
            message=message,
        )
        Posts.create(data)

    def send_reply_treads(self, message):
        """
        1) Смотрим информацию о треде, на который была реакция
        2) Если в root_id нет данных(False), то значит реакцию поставили на ПЕРВОЕ сообщение в канале
         2.1) - Отправляем сообщение подставляя в root_id информацию из data.reaction.post_id (из события по реакции)
        3) Если  в root_id есть данные(True), то значит реакцию поставили на сообщение ВНУТРИ треда
         3.1) - Отправляем сообщение подставляя в root_id информацию из response.root_id (то , что пришло в ответе о треде)

         Итого мы теперь можем отправлять сообщения в треде, когда ставят реакцию не только на ПЕРВОЕ сообщение, но и
         на сообщения внутри самого треда
        """
        response_api_get_info_about_post = Posts.get_info_about_post(self.data.reaction.post_id)
        get_post = GetPostResponse(
            root_id=response_api_get_info_about_post.get('root_id')
        )
        if not get_post.root_id:
            self.reply(root_id=self.data.reaction.post_id, message=message)
        if get_post.root_id:
            self.reply(root_id=get_post.root_id, message=message)
