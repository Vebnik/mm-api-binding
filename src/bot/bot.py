from typing import Callable

from src.bot.schemas import BotConfig, Event
from src.bot.utils import Logger
#
from src.ws.ws import WSGateway

class Bot:

    handlers: dict[str, Callable] = {}
    config: BotConfig

    def __init__(self, config: BotConfig) -> None:
        self.config = config

    def run(self) -> None:
        WSGateway.init(self.config, self.handlers)

    def listen(self, action: str) -> Callable:
        def wrapper(func):

            Logger.info(f'Register listener to -> {action} | {func.__name__}')

            self.handlers[action] = func

            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            return inner
        return wrapper
    