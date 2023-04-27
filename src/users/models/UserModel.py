from app.settings.components import BaseModel
from tortoise import fields


class User(BaseModel):
    """Модель пользователя"""

    vk_id = fields.IntField(unique=True)
    name = fields.TextField()
    level = fields.IntField(default=1)
    exp = fields.IntField(default=0)
    date_reg = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'users'

    def __str__(self):
        """Строковое представление модели"""
        return f'{self.id} | {self.name}'
