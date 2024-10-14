from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


load_dotenv()

keyboard =ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Котики'),KeyboardButton(text='Собачки')],
    [KeyboardButton(text='Погода'), KeyboardButton(text='Гороскоп')],
],
    resize_keyboard=True,
    input_field_placeholder='Выбери'
)