from vkbottle import Bot
from app.settings import DEBUG
from app.settings.components import middlewares, db_models, db_url, apps

from loguru import logger
from tortoise import Tortoise, run_async


async def init_db() -> None:
    """Инициализация базы данных"""
    await Tortoise.init(
        db_url=db_url,
        modules={'models': db_models},
    )


async def init_bot(bot: Bot) -> None:
    """Инициализация бота"""
    if apps:
        for app in apps:
            for labeler in app:
                labeler.load(bot)

    if middlewares:
        for middleware in middlewares:
            bot.labeler.message_view.register_middleware(middleware)

    if DEBUG is False:
        logger.disable('vkbottle')
        print('[INFO] BOT STARTED')


if __name__ == '__main__':
    from app.settings.components import bot
    bot.loop_wrapper.on_startup.append(init_bot(bot))
    run_async(init_db())
    bot.run_forever()
