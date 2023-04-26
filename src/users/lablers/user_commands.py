from vkbottle.bot import Blueprint, Message

bp = Blueprint('user_commands')


@bp.on.private_message(text=['hello', 'привет'])
async def test_function(message: Message):
    """Тестовая команда"""
    return await message.reply('Hello my friend!')
