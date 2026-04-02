from src.scraper import scrape_book

if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    
    data = scrape_book(url)
    
    print(data)