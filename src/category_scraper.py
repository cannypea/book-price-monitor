import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

def get_book_links(category_url):
    book_links = []

    while True:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            rel_link = article.find("h3").find("a")["href"]
            full_link = urljoin(category_url, rel_link)
            book_links.append(full_link)

        # Handle pagination
        next_btn = soup.find("li", class_="next")
        if not next_btn:
            break

        next_page = next_btn.find("a")["href"]
        category_url = urljoin(category_url, next_page)

    return book_links