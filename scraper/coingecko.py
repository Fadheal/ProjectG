import requests
from bs4 import BeautifulSoup

def pixels_coin():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'From': 'fadheeal@gmail.com'
    }

    sesion = requests.Session()
    sesion.headers.update(headers)

    r = sesion.get("https://www.coingecko.com/en/coins/pixels")
    soup = BeautifulSoup(r.text, "html.parser")

    price = soup.find("div", class_="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-3xl md:tw-text-4xl tw-leading-10").find("span").get_text(strip=True)
    print(price)
    return price