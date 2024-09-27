import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from app.hendlers import router
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.scheduler import schedule_good_morning


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router=router)
    scheduler = AsyncIOScheduler()
    schedule_good_morning(scheduler=scheduler, bot=bot)
    scheduler.start()
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')



