import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from app.hendlers import router
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.scheduler import schedule_good_morning
from database import init_db
from load_txt import load_texts
from models.good_morning import Good_Morning
from models.good_night import Good_Night


async def main():
    load_dotenv()
    TOKEN = str(os.getenv('TOKEN'))
    if not TOKEN or not isinstance(TOKEN, str):
        logging.error("not TOKEN")
    else:
        logging.info(f"token:{TOKEN}")
    bot = Bot(token=str(TOKEN))
    dp = Dispatcher()
    dp.include_router(router=router)

    scheduler = AsyncIOScheduler()
    schedule_good_morning(scheduler=scheduler, bot=bot)
    scheduler.start()
    await init_db()
    await load_texts('./data/text_night.txt', Good_Night)
    await load_texts('./data/text_morning.txt', Good_Morning)
    await dp.start_polling(bot)




if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print('Exit')



