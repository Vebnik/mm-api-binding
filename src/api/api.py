from typing import Any
from os import getenv
from requests import request

from src.bot.utils import Logger
from src.api.schemas import Endpoints, PostData

class Client:

    root_url: str = getenv('ENDPOINT', '')
    token: str = getenv('TOKEN', '')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    @classmethod
    def execute(cls, command: str, method: str, data: Any = {}) -> Any:
        try:
            if method in ['post', 'patch', 'put']:
                response = request(method, f'{cls.root_url}{command}', json=data, headers=cls.headers)
                Logger.info('Execute api')

            if method in ['get', 'delete']:
                response = request(method, f'{cls.root_url}{command}', headers=cls.headers)
                Logger.info('Execute api')

        except Exception as ex:
            Logger.error(ex)


class Posts:

    @classmethod
    def create(cls, post_data: PostData) -> Any:
        data = post_data.model_dump()
        Client.execute(Endpoints.create_post, 'post', data)

    @classmethod
    def add_reaction(cls, post_data: PostData) -> Any:
        data = post_data.model_dump()
        Client.execute(Endpoints.create_post, 'post', data)

    @classmethod
    def get(cls) -> Any:
        ...