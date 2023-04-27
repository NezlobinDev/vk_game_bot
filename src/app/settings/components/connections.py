from app.settings import env
from vkbottle import Bot
from vkbottle.bot import Message

GROUP_TOKEN = env('GROUP_TOKEN', default=None)

bot = Bot(token=GROUP_TOKEN)
Message.bot = bot
