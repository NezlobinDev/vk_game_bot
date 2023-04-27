from tortoise.models import Model
from tortoise import fields

from app.settings import env

SQL_HOST = env('SQL_HOST', default=None)
SQL_USER = env('SQL_USER', default=None)
SQL_BASE = env('SQL_BASE', default=None)
SQL_PASSWORD = env('SQL_PASSWORD', default=None)

DB_URL = f'mysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_BASE}'

MODELS = [
    'aerich.models',
    'users.models',
]

TORTOISE_ORM = {
    'connections': {
        'default': DB_URL,
    },
    'apps': {
        'my_app': {
            'models': MODELS,
            'default_connection': 'default',
        }
    },
    'use_tz': False,
    'timezone': 'UTC'
}


class BaseModel(Model):
    """Базовая модель"""

    id = fields.IntField(pk=True)
