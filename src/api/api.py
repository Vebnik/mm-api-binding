from typing import Any
from requests import Session

from src.bot.utils import Logger
from src.bot.schemas import BotConfig
from src.api.schemas import Endpoints


class Client:

    root_url: str
    session: Session

    @classmethod
    def init(cls, config: BotConfig):
        cls.session = Session()
        cls.root_url = config.api_endpoint
        cls.session.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config.token}'
        }

    @classmethod
    def execute(cls, endpoint: str, method: str, data: dict|list = {}) -> Any:
        try:
            response = cls.session.request(method, f'{cls.root_url}{endpoint}', json=data)

            if response.ok:
                return response.json()
        except Exception as ex:
            Logger.error(ex)

    @classmethod
    def get_client_info(cls, client_user_id: str) -> Any:
        data = [client_user_id]
        return cls.execute(Endpoints.get_users_by_ids, 'get', data)
