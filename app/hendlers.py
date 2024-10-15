import os
import requests

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from models.user import User
from database import AsyncSessionLocal, get_session
from  sqlalchemy.future import select
from .signs_zodiac import Form, ZODIAC_SIGNS
from .keyboard import keyboard
from .parser import parser


router = Router()
load_dotenv()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where (User.user_id == user_id))
        existing_user = result.scalars().first()
        if existing_user is None:
            new_user = User(user_id=user_id, name=user_name)
            session.add(new_user)
            await session.commit()
        await message.answer(f'Привет {message.from_user.first_name}!!!!!!')
        await message.answer("Напиши свой знак зодиака")
        await state.set_state(Form.waiting_for_zodic)
        await sign_zodiac()
        await state.clear()
        await message.reply(f'Выбери {message.from_user.first_name}', reply_markup=keyboard)


@router.message(Form.waiting_for_zodic)
async def sign_zodiac(message:Message):
    user = message.text.lower().strip()
    user_id = message.from_user.id
    async for session in get_session():
        if user in ZODIAC_SIGNS:
            user_zodiac = ZODIAC_SIGNS[user]
            result = await session.execute(select(User).where(User.user_id == user_id))
            user_res = result.scalar_one_or_none()
            user_res.zodiac_sign = user_zodiac
            await session.commit()
            await message.reply("Спасибо")


@router.message(F.text=='Гороскоп')
async def buttom_goroscope(message: Message):
    id = message.from_user.id
    async for session in get_session():
        result = await session.execute(select(User).where(User.user_id == id))
        sign_user = result.scalar_one_or_none()
        text_goroscope = await parser(sign_user.zodiac_sign)
        await message.answer(f'Твой гороскоп на сегодня {sign_user.zodiac_sign} \U0001F618 \n {text_goroscope}')


@router.message(F.text=='Погода')
async def get_weather(message: Message):
    """Реализация кнопки погоды"""
    weather_token = os.getenv('WEATHER_TOKEN')
    city = 'Воронеж'
    url = (f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={weather_token}')
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    description = weather_data['weather']
    des = description[0]
    wint = weather_data['wind']['speed']
    w_now = 'Сейчас в городе ' + city + ' ' + str(temperature) + ' °C'
    w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'
    w_description = 'Сейчас в городе ' + des['description']
    w_wint = (f'Скорость ветра {str(wint)} м/с')
    await message.answer(f'{w_now}🌡️ \n{w_feels}🌡️  \n{w_description}🏙️ \n{w_wint}💨')

                                    
@router.message((F.text=='Котики') | (F.text=='Собачки'))
async def buttom_img(message:Message):
    mes = message.text
    if mes == 'Котики':
        photo_kotic_url = 'https://api.thecatapi.com/v1/images/search'
        url_pic = photo_kotic_url
        emoji = '\U0001F408 \U0001F431 '

    elif mes == 'Собачки':
        photo_dog_url = 'https://api.thedogapi.com/v1/images/search'
        url_pic = photo_dog_url
        emoji = '\U0001F436 \U0001F415'

    url_photo= requests.get(url=url_pic).json()
    photo = url_photo[0]['url']
    await message.answer_photo(photo=photo, caption=f'\U00002764 \U0001F618 Специально для тебя {emoji}')



