import requests

from database import get_session
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql.expression import func
from models.user import User
from models.good_morning import Good_Morning
from models.good_night import Good_Night


async def get_users_all(session: AsyncSession):
    result = await session.execute(select(User))
    user = result.scalars().all()
    return user


async def get_text_good_morning_all(session: AsyncSession, model):
    result = await session.execute(select(model).order_by(func.random()).limit(1))
    text = result.scalar_one_or_none()
    return text.text


async def send_good(bot, model, imogi_1, imogi_2):
    async for session in get_session():
        users = await get_users_all(session)
        text = await get_text_good_morning_all(session, model)
        for user in users:
            await bot.send_message(chat_id=user.user_id, text=f'{imogi_1} {user.name} {text} {imogi_2}')
            await send_image(bot, user.user_id)


async def send_image(bot, user_id):
    image_url = 'https://api.thecatapi.com/v1/images/search'
    get_photo = requests.get(image_url).json()
    photo = get_photo[0]['url']
    await bot.send_photo(user_id, photo=photo, caption=f'А это специально для тебя \U00002764 \U0001F618')


def schedule_good_morning(scheduler: AsyncIOScheduler, bot):
    scheduler.add_job(
        send_good, 'cron', hour=18, minute=48, args=[bot, Good_Morning, '\U0001F305', '\U00002615'])
    scheduler.add_job(
        send_good, 'cron', hour=18, minute=48, args=[bot, Good_Night, '\U0001F634', '\U0001F4A4 \U0001F319'])