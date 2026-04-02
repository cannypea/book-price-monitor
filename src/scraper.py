import requests
from bs4 import BeautifulSoup

def scrape_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text

    price = soup.find("p", class_="price_color").text

    return {
        "title": title,
        "price": price
    }