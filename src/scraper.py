import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"

def get_rating(soup):
    rating_tag = soup.find("p", class_="star-rating")
    classes = rating_tag.get("class")
    return classes[1]  # e.g., "Three"

def get_category(soup):
    breadcrumb = soup.find("ul", class_="breadcrumb")
    return breadcrumb.find_all("li")[2].text.strip()

def scrape_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title = soup.find("h1").text

    # Product info table
    table = soup.find("table")
    rows = table.find_all("tr")

    product_data = {}
    for row in rows:
        key = row.find("th").text
        value = row.find("td").text
        product_data[key] = value

    # Description
    desc_tag = soup.find("div", id="product_description")
    if desc_tag:
        description = desc_tag.find_next_sibling("p").text
    else:
        description = ""

    # Image URL
    image_rel = soup.find("img")["src"]
    image_url = BASE_URL + image_rel.replace("../../", "")

    return {
        "product_page_url": url,
        "universal_product_code": product_data.get("UPC"),
        "book_title": title,
        "price_including_tax": product_data.get("Price (incl. tax)"),
        "price_excluding_tax": product_data.get("Price (excl. tax)"),
        "quantity_available": product_data.get("Availability"),
        "product_description": description,
        "category": get_category(soup),
        "review_rating": get_rating(soup),
        "image_url": image_url,
    }