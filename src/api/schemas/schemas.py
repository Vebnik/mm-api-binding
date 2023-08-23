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


class PostData(BaseModel):
    channel_id: str
    message: str
    root_id: str | None = ''
    file_ids: list[str] | list[None] = []
    props: dict | None = {}
    metadata: dict | None = {}
