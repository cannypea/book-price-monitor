from src.scraper import scrape_book
import pandas as pd

if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

    data = scrape_book(url)

    df = pd.DataFrame([data])
    df.to_csv("book_data.csv", index=False)

    print("Data saved to book_data.csv")