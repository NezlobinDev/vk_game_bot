from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from users.models import User


class UserRegistrationMiddleware(BaseMiddleware[Message]):
    """Мидлварь регистрации пользователя в системе"""

    def __init__(self, event, view):
        super().__init__(event, view)

    async def pre(self):
        user_id = self.event.from_id
        if not await User.filter(vk_id=user_id).exists():
            user_name = await Message.bot.api.users.get(user_id)
            Message.user = await User.create(vk_id=user_id, name=user_name[0].first_name)
            BaseMiddleware.user = Message.user

            # self.stop() - Прирывание. после успешной регистрации не пускаем юзера дальше
            # TODO: Перед прирыванием отправим юзера знакомится с системами/проходить сюжетку
            self.stop(f'Пользователь id:{Message.user.id} успешно зарегистрирован!')
