import os
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy.future import select
from models.user import User

load_dotenv()

keyboard =ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Котики'),KeyboardButton(text='Собачки')],
    [KeyboardButton(text='Погода'), KeyboardButton(text='Гороскоп')],
],
    resize_keyboard=True,
    input_field_placeholder='Выбери'
)

# async def get_user_zodiac(id:int, session: AsyncSession):
#     # async for session in get_session():
#     get_zodiac = await session.execute(select(User).where(User.user_id==id))
#     result = get_zodiac.scalars().first()
#     print(result, '11111111111111111111111111111111111111')
#     url = (f'https://horoscope.sakh.com/{result.zodiac_sign}')
#     keyboard=InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Котики', callback_data="котики"),
#         InlineKeyboardButton(text='Собачки', callback_data="собачки")],
#         [InlineKeyboardButton(text='Погода', callback_data="погода"),
#         InlineKeyboardButton(text='Гороскоп', url=url)]
#     ])
#
#     return keyboard



