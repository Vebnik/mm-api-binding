from typing import Any
from os import getenv
from requests import request

from src.bot.utils import Logger
from src.api.schemas.schemas import Endpoints, PostData
from src.api.schemas.get_post_response import GetPostResponse


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
                if response.status_code not in (200, 201):
                    Logger.info(f'Ответ от апи {response.status_code}. Text: {response.text}')
            if method in ['get', 'delete']:
                response = request(method, f'{cls.root_url}{command}', headers=cls.headers)
                if response.status_code not in (200, 201):
                    Logger.info(f'Ответ от апи {response.status_code}. Text: {response.text}')
                Logger.info('Execute api')
                return response.json()


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
    def get_info_about_post(cls, post_id) -> GetPostResponse:
        response = Client.execute(f'{Endpoints.get_a_post}{post_id}', 'get')
        return response
