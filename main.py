from src.scraper import scrape_book
from src.category_scraper import get_book_links
import pandas as pd

if __name__ == "__main__":
    category_url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

    links = get_book_links(category_url)

    all_data = []

    for link in links:
        try:
            data = scrape_book(link)
            all_data.append(data)
        except Exception as e:
            print(f"Error scraping {link}: {e}")

    df = pd.DataFrame(all_data)
    df.to_csv("category_books.csv", index=False)

    print("Category data saved to category_books.csv")