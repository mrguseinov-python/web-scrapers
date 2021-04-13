import requests
from bs4 import BeautifulSoup

store_types = ["woman", "men", "lingerie", "shoes-and-bags", "sport"]

unique_stores = set()
for store_type in store_types:
    page = requests.get(f"https://www.galeria.spb.ru/{store_type}/?utm_view=list")

    soup = BeautifulSoup(page.text, "lxml")
    stores = soup.find_all("a", class_="shops-list__link")
    stores = [store.text.strip() for store in stores]

    unique_stores.update(stores)

with open("stores.txt", "w") as file:
    file.writelines([store + "\n" for store in sorted(unique_stores, key=str.lower)])
