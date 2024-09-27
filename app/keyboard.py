import os
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

load_dotenv()

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


users_keyboard={439845524: 'virgo',1978591255: 'leo'}


async def get_goroscope(id):
    """Принимает id пользователя и выбирает кому какой гороскоп присылать"""
    url = (f'https://horoscope.sakh.com/{users_keyboard[id]}')
    mini_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Гороскоп', url=url)]
    ])
    return mini_keyboard

