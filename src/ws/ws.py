from typing import Callable, Any
from websocket import WebSocketApp
import rel, websocket, json

from src.bot.schemas import BotConfig
from src.bot.utils import Logger
from src.ws.schemas.base import event_model, BaseEvent


class WSGateway:

    handlers: dict[str, Callable] = {}
    config: BotConfig

    @classmethod
    def on_message(cls, ws: WebSocketApp, message: str) -> None:
        Logger.info('New Message')

        event_message: dict = json.loads(message)
        event_name = event_message.get('event', '')

        if event_name:
            if not event_model.get(event_name): return
            event: BaseEvent = event_model[event_name].model_validate(event_message)

            if not cls.handlers.get(event.event): 
                Logger.info(f'Not found handler for "{event.event}" event')
                return
            
            cls.handlers[event.event](event)

    @classmethod
    def on_error(cls, ws: WebSocketApp, error) -> None:
        Logger.error(error)

    @classmethod
    def on_close(cls, ws: WebSocketApp, close_status_code, close_msg) -> None:
        Logger.info("Closed connection")

    @classmethod
    def on_open(cls, ws: WebSocketApp) -> None:
        Logger.info("Opened connection")

        auth_data = {
            "seq": 1,
            "action": "authentication_challenge",
            "data": {
                "token": cls.config.token
            }
        }

        ws.send(data=json.dumps(auth_data))

    @classmethod
    def init(cls, config: BotConfig, handlers: dict[str, Callable]) -> None:
        Logger.info('Try to init ws')

        cls.handlers = handlers
        cls.config = config

        websocket.enableTrace(False)

        ws = WebSocketApp(
            config.endpoint,
            on_open=cls.on_open,
            on_message=cls.on_message,
            on_error=cls.on_error,
            on_close=cls.on_close
        )

        ws.run_forever(dispatcher=rel, reconnect=5)
        rel.signal(2, rel.abort)
        rel.dispatch()

