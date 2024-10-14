import requests

from database import get_session
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy.future import select
from models.user import User

users= (439845524,1978591255,)
async def get_users_all(session: AsyncSession):
    result = await session.execute(select(User))
    user = result.scalars().all()
    return user


async def send_good_morning(bot):
    async for session in get_session():
        users = await get_users_all(session)
        for user in users:
            print(user.name)
            await bot.send_message(chat_id=user.user_id, text=f'\U0001F305 Доброе утро {user.name} \U00002615')
            await send_image(bot, user.user_id)


async def send_image(bot, user_id):
    image_url = 'https://api.thecatapi.com/v1/images/search'
    get_photo = requests.get(image_url).json()
    photo = get_photo[0]['url']
    await bot.send_photo(user_id, photo=photo, caption=f'А это специально для тебя \U00002764 \U0001F618')


def schedule_good_morning(scheduler: AsyncIOScheduler, bot):
    scheduler.add_job(send_good_morning, 'cron', hour=6, minute=00, args=[bot])