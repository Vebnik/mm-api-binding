from typing import Callable, Any
from websocket import WebSocketApp

from src.bot.schemas import BotConfig
from src.bot.utils import Logger
from src.ws.ws import WSGateway
from src.api.api import Client


class Bot:

    handlers: dict[str, Callable] = {}
    config: BotConfig
    ws = WSGateway
    client = Client

    def __init__(self, config: BotConfig) -> None:
        self.config = config

    def run(self) -> None:
        self.client.init(self.config)
        self.ws.init(self.config, self.handlers)

    def listen(self, action: str) -> Callable:
        def wrapper(func) -> Callable:

            Logger.info(f'Register listener to -> {action} | {func.__name__}')

            def proxy(event, bot = self):
                func(event, bot)

            self.handlers[action] = proxy

            def inner(*args, **kwargs) -> Any:
                return func(*args, **kwargs)
            
            return inner
        return wrapper
    