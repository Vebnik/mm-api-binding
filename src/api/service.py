from src.api.schemas import Endpoints, PostData, ReactionData
from src.api.api import Client


class Posts:

    @classmethod
    def create(cls, post_data: PostData) -> None:
        data = post_data.model_dump()
        Client.execute(Endpoints.create_post, 'post', data)

    @classmethod
    def add_reaction(cls, reaction_data: ReactionData) -> None:
        data = reaction_data.model_dump()
        Client.execute(Endpoints.create_reaction, 'post', data)

    @classmethod
    def get(cls) -> None:
        ...