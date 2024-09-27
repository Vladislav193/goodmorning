from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

keyboard =ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Котики'),KeyboardButton(text='Собачки')],
    [KeyboardButton(text='Погода')],
],
    resize_keyboard=True,
    input_field_placeholder='Выбери'
)
#
# mini_keyboard=InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Гороскоп', url=f'https://horoscope.sakh.com/{user[id]}')]
# ])





async def get_goroscope(id):
    """Принимает id пользователя и выбирает кому какой гороскоп присылать"""
    url = (f'https://horoscope.sakh.com/{users[id]}')
    mini_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Гороскоп', url=url)]
    ])
    return mini_keyboard

