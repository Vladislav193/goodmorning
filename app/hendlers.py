import os

import app.keyboard as bt
import requests
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

router = Router()
load_dotenv()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Доброе утро {message.from_user.first_name}!!!!!!',
                        reply_markup=await bt.get_goroscope(message.from_user.id))

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Buttom help')

@router.message(F.text=='Погода')
async def get_weather(message: Message):
    """Реализация кнопки погоды"""
    weather_token = os.getenv('WEATHER_TOKEN')
    city = 'Воронеж'
    url = (f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={weather_token}')
    weather_data = requests.get(url).json()
    # получаем данные о температуре и о том, как она ощущается
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    # формируем ответы
    w_now = 'Сейчас в городе ' + city + ' ' + str(temperature) + ' °C'
    w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'
    # отправляем значения пользователю
    await message.answer(f'{w_now} \n{w_feels}')



@router.message(F.text=='Котики')
async def how_are_you(message:Message):
    await message.answer('Good')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
