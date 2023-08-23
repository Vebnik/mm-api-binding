from dotenv import load_dotenv; load_dotenv()
from os import getenv

from src.bot.bot import Bot
from src.bot.schemas import BotConfig, Event
from src.ws.schemas import reaction_added


def main() -> None:
    config = BotConfig(
        token=getenv('TOKEN') or '',
        endpoint=getenv('WS_ENDPOINT') or ''
    )

    bot = Bot(config)

    @bot.listen(action=Event.reaction_added)
    def on_new_post_to_reaction(event: reaction_added.ReactionAddedEvent) -> None:
        if event.data.reaction.channel_id == f"{getenv('CHANNEL_ID')}" and event.data.reaction.emoji_name == f"{getenv('EMOJI_NAME')}":
            print('Реакция ⭐ была поставлена в test_channel')
            event.send_reply_treads("Ответ на реакцию ⭐ + @tag ")


    bot.run()


if __name__ == '__main__':
    main()
