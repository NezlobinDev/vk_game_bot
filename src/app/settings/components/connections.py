from app.settings import env
from vkbottle import Bot

GROUP_TOKEN = env('GROUP_TOKEN', default=None)
SQL_HOST = env('SQL_HOST', default=None)
SQL_USER = env('SQL_USER', default=None)
SQL_BASE = env('SQL_BASE', default=None)
SQL_PASSWORD = env('SQL_PASSWORD', default=None)

bot = Bot(token=GROUP_TOKEN)
db_url = f'mysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_BASE}'
