from pydantic import BaseModel


class Endpoints:

    # service
    api_ver = 'v4'

    # posts
    create_post = f'/api/{api_ver}/posts'
    get_a_post = f'/api/{api_ver}/posts/'

    # channels
    get_all_channels = f'/api/{api_ver}/channels'
    get_a_channel = f'/api/{api_ver}/channels/'

    # reactions
    create_reaction = f'/api/{api_ver}/reactions'

    # users
    get_users_by_ids = f'/api/{api_ver}/users/ids'


class PostData(BaseModel):
    channel_id: str
    message: str
    root_id: str | None = ''
    file_ids: list[str] | list[None] = []
    props: dict | None = {}
    metadata: dict | None = {}


class ReactionData(BaseModel):
    user_id: str
    post_id: str
    emoji_name: str
    create_at: int = 0

