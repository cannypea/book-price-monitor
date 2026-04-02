from src.site_scraper import get_categories
from src.category_scraper import get_book_links
from src.scraper import scrape_book
from src.image_downloader import download_image

import pandas as pd
import os
import time


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

                time.sleep(0.5)  # polite delay

            except Exception as e:
                print(f"Error scraping {link}: {e}")

        # AFTER finishing the category, save CSV
        safe_name = category_name.replace(" ", "_").lower()
        file_path = f"data/{safe_name}.csv"

        df = pd.DataFrame(all_data)
        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")