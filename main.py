import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from app.hendlers import router
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.scheduler import schedule_good_morning


async def main():
    load_dotenv()
    TOKEN = str(os.getenv('TOKEN'))
    bot = Bot(token=TOKEN)
    if not TOKEN:
        logging.error("not TOKEN")
    else:
        logging.info(f"token:{TOKEN}")
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



