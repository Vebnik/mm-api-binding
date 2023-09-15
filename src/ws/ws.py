from typing import Callable, Any, Type
from websocket import WebSocketApp
import rel, websocket, json

from src.bot.schemas import BotConfig
from src.bot.utils import Logger
from src.ws.schemas.base import event_model


class WSGateway:

    handlers: dict[str, Callable] = {}
    config: BotConfig
    client_info: dict

    @classmethod
    def on_message(cls, ws: WebSocketApp, message: str) -> None:
        Logger.info('New Message')

        event_message: dict = json.loads(message)
        event_name = event_message.get('event')

        if not event_name: return

        match event_name:
            case 'hello':
                cls.client_info = event_message.get('broadcast', {})
            case _:
                cls.handlers[event_name](event_model[event_name].model_validate(event_message))
                
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
        Logger.info('Init ws')

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

