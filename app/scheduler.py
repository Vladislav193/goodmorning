import requests

from apscheduler.schedulers.asyncio import AsyncIOScheduler


users= (439845524,1978591255,)

async def send_good_morning(bot):
    for user_id in users:
        await bot.send_message(chat_id=user_id, text=f'\U0001F305 Доброе утро \U00002615')
        await send_image(bot, user_id)


async def send_image(bot, user_id):
    image_url = 'https://api.thecatapi.com/v1/images/search'
    get_photo = requests.get(image_url).json()
    photo = get_photo[0]['url']
    await bot.send_photo(user_id, photo=photo, caption=f'А это специально для тебя \U00002764 \U0001F618')
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(photo) as resp:
    #         if resp.status == 200:
    #             img_data = await resp.read()



def schedule_good_morning(scheduler: AsyncIOScheduler, bot):
    scheduler.add_job(send_good_morning, 'cron', hour=6, minute=00, args=[bot])
