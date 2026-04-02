import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

def get_categories():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    category_dict = {}

    category_section = soup.find("ul", class_="nav nav-list")
    links = category_section.find_all("a")

    for link in links:
        name = link.text.strip()
        
        # Skip "Books" (main category)
        if name.lower() == "books":
            continue

        href = link["href"]
        full_url = urljoin(BASE_URL, href)

        category_dict[name] = full_url

    return category_dict