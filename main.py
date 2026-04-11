import logging
import os
import time
import pandas as pd
from src.site_scraper import get_categories
from src.category_scraper import get_book_links
from src.scraper import scrape_book
from src.image_downloader import download_image


# Configure logging
os.makedirs("logs", exist_ok=True)  # optional: save logs in a folder
logging.basicConfig(
    filename="logs/scraper.log",  # log file path
    level=logging.INFO,            # log all info and above
    format="%(asctime)s [%(levelname)s] %(message)s",
)


if __name__ == "__main__":
    categories = get_categories()

    # Create data folder
    os.makedirs("data", exist_ok=True)

    for category_name, category_url in categories.items():
        print(f"Scraping category: {category_name}")

        links = get_book_links(category_url)
        all_data = []

        # LOOP THROUGH BOOK LINKS (inside category loop)
        for link in links:
            try:
                data = scrape_book(link)
                all_data.append(data)

                # Download image
                download_image(
                    data["image_url"],
                    category_name.replace(" ", "_").lower(),
                    data["universal_product_code"]
                )
                logging.info(f"Successfully scraped {link}")
                time.sleep(0.5)  # polite delay

            except Exception as e:
                logging.error(f"Failed to scrape {link}: {e}")

        # AFTER finishing the category, save CSV
        safe_name = category_name.replace(" ", "_").lower()
        file_path = f"data/{safe_name}.csv"

        df = pd.DataFrame(all_data)
        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")