from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import csv
import Seleniumtest


url = "https://arbuz.kz/ru/almaty/catalog/cat/225178-ovoshi#/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
items = soup.find_all("article", {"class": "product-item product-card"})

with open("swag1.txt", "w", encoding="utf-8") as f:
    writer = csv.writer(f)

    for item in items:
        title = item.find("a", {"class": "product-card__title"}).text.strip()
        link = item.find("a", {"class": "product-card__title"}).get("href")
        price = link.find("b")
        data = [title, price, f"https://arbuz.kz/ru{link}"]
        writer.writerow(data)
        print(f"title: {title} | {price} | https://arbuz.kz/ru{link}") 
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
