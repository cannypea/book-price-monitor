import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"


def get_rating(soup) -> str:
    rating_tag = soup.find("p", class_="star-rating")
    if rating_tag:
        classes = rating_tag.get("class", [])
        if len(classes) > 1:
            return classes[1]
    return "None"


def get_category(soup) -> str:
    breadcrumb = soup.find("ul", class_="breadcrumb")
    if breadcrumb:
        items = breadcrumb.find_all("li")
        if len(items) > 2:
            return items[2].text.strip()
    return "Unknown"


def get_quantity(product_data: dict) -> str:
    availability = product_data.get("Availability", "")
    match = re.search(r"\d+", availability)
    return match.group() if match else "0"


def scrape_book(url: str) -> dict[str, str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else "Unknown"

    # Product info table
    product_data = {}
    table = soup.find("table")
    if table:
        rows = table.find_all("tr")
        for row in rows:
            th = row.find("th")
            td = row.find("td")
            if th and td:
                product_data[th.text.strip()] = td.text.strip()

    # Description
    desc_tag = soup.find("div", id="product_description")
    if desc_tag:
        desc_p = desc_tag.find_next_sibling("p")
        description = desc_p.text.strip() if desc_p else ""
    else:
        description = ""

    # Image URL (robust handling)
    image_tag = soup.find("img")
    if image_tag and image_tag.get("src"):
        image_url = urljoin(BASE_URL, image_tag["src"])
    else:
        image_url = ""

    return {
        "product_page_url": url,
        "universal_product_code": product_data.get("UPC", ""),
        "book_title": title,
        "price_including_tax": product_data.get("Price (incl. tax)", ""),
        "price_excluding_tax": product_data.get("Price (excl. tax)", ""),
        "quantity_available": get_quantity(product_data),
        "product_description": description,
        "category": get_category(soup),
        "review_rating": get_rating(soup),
        "image_url": image_url,
    }