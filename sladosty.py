from attr import asdict
from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
from fake_useragent import UserAgent
import csv

BASE_URL = "https://arbuz.kz/ru/collections/248748-chai_kofe_sladosti#/"


header = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=header) as response:
            r = await response.content.read()
            soup = BeautifulSoup(r, "html.parser")
            items = soup.find_all("article", {"class": "product-item product-card"})
            with open("output.txt", "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                for item in items:
                    title = item.find("a", {"class": "product-card__title"}).text.strip()
                    link = item.find("a", {"class": "product-card__title"}).get("href")
                    price = item.find("b").text.strip()
                    data = [title, price, f"https://arbuz.kz/ru{link}"]
                    writer.writerow(data)
                    print(f"title: {title} | {price} | https://arbuz.kz/ru{link}")

    
                 

    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())