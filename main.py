from dotenv import load_dotenv; load_dotenv()
from os import getenv

from src.bot.bot import Bot
from src.bot.schemas import BotConfig, Event
from src.ws.schemas import HelloEvent, PostedEvent


def main() -> None:
    config = BotConfig(
        token=getenv('TOKEN') or '',
        endpoint=getenv('WS_ENDPOINT') or ''
    )

    bot = Bot(config)

    @bot.listen(action=Event.hello)
    def on_hello(event: HelloEvent) -> None:
        print(event.data.connection_id)

    @bot.listen(action=Event.posted)
    def on_new_message(event: PostedEvent) -> None:
        print(f'Message from {event.data.channel_display_name} | type {event.data.channel_type}')

    bot.run()


if __name__ == '__main__':
    main()