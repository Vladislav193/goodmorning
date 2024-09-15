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
    await message.answer("Почему не здороваемся?")


@router.message(F.text=='Привет' or F.text=='Хай' or F.text=='Здравствуй')
async def start_but(message: Message):
    await message.reply(f'Так-то лучше {message.from_user.first_name}',
        reply_markup = bt.keyboard)


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
    description = weather_data['weather']
    des = description[0]
    wint = weather_data['wind']['speed']
    # формируем ответы
    w_now = 'Сейчас в городе ' + city + ' ' + str(temperature) + ' °C'
    w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'
    w_description = 'Сейчас в городе ' + des['description']
    w_wint = (f'Скорость ветра {str(wint)} м/с')
    # отправляем значения пользователю
    await message.answer(f'{w_now} \n{w_feels} \n{w_description} \n{w_wint}')

                                    
@router.message(F.text=='Котики')
async def how_are_you(message:Message):
    photo_kotic_url = 'https://api.thecatapi.com/v1/images/search'
    url_photo= requests.get(url=photo_kotic_url).json()
    photo1 = url_photo[0]
    photo = photo1['url']
    print(photo)
    await message.answer_photo(photo=photo)


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
