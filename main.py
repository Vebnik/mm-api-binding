from dotenv import load_dotenv; load_dotenv()
from os import getenv

from src.bot.bot import Bot
from src.bot.schemas import BotConfig, Event
from src.ws.schemas import posts



def main() -> None:
    config = BotConfig(
        token=getenv('TOKEN') or '',
        endpoint=getenv('WS_ENDPOINT') or ''
    )

    bot = Bot(config)

    @bot.listen(action=Event.posted)
    def on_new_post(event: posts.PostedEvent) -> None:
        event.reply('Nice iphone')

    bot.run()


if __name__ == '__main__':
    main()
