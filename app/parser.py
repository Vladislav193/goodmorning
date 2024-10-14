import requests
from bs4 import BeautifulSoup

async def parser(sign):
# URL страницы с гороскопом для Девы
    url = f"https://1001goroskop.ru/?znak={sign}"

    # Заголовки для имитации запроса из браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # Отправляем GET-запрос на сайт
    response = requests.get(url, headers=headers)


# Ищем элемент <div> с атрибутом itemprop="description"
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем элемент <div> с атрибутом itemprop="description"
        description_div = soup.find('div', {'itemprop': 'description'})
        if description_div:
            # Извлекаем текст внутри <div>
            horoscope_text = description_div.get_text(strip=True)
    return horoscope_text