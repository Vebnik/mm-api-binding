from dotenv import load_dotenv; load_dotenv()
from os import getenv

from src.bot.bot import Bot
from src.bot.schemas import BotConfig, Event
from src.ws.schemas import posts, reactions


def main() -> None:
    config = BotConfig(
        token=getenv('TOKEN') or '',
        endpoint=getenv('WS_ENDPOINT') or '',
        api_endpoint=getenv('ENDPOINT') or '',
    )

    bot = Bot(config)

    @bot.listen(action=Event.posted)
    def on_new_post(event: posts.PostedEvent, bot: Bot) -> None:
        print(event)

        info = bot.client.get_client_info(bot.ws.client_info.get('user_id'))
        print(info)

    @bot.listen(action=Event.reaction_added)
    def on_add_reaction(event: reactions.ReactionAddedEvent, bot: Bot) -> None:
        print(bot)
        # event.reply('Nice iphone')

    bot.run()


if __name__ == '__main__':
    main()

