markdown
## Book Price Monitoring System and Market analysis
A Python-based web scraping application that extracts book data and pricing information from **Books to Scrape**. This project simulates a beta version of a price monitoring system for an online bookstore and is designed as a foundation for a scalable **ETL (Extract, Transform, Load) pipeline**.


## Project Overview
The application performs large-scale data extraction by:

- Scraping book details from an online retailer
- Organizing data by category
- Exporting structured datasets (CSV)
- Downloading and storing product images

It is modular, reusable, and suitable for automating monitoring of book prices and other product data.

## Features
- Extracts:
  - Product page URL  
  - Universal Product Code (UPC)  
  - Book title  
  - Price (including & excluding tax)  
  - Quantity available  
  - Product description  
  - Category  
  - Review rating  
  - Image URL  
- Supports:
  - Pagination handling  
  - Multi-category scraping  
  - Image downloading & organization  
  - Clean CSV output per category  

## Project Structure
book-price-monitor/
│
├── data/                  # Output CSV files (ignored in Git)
├── images/                # Downloaded images (ignored in Git)
│
├── src/
│   ├── scraper.py          # Scrapes individual book data
│   ├── category_scraper.py # Gets book links from a category
│   ├── site_scraper.py     # Extracts all categories
│   ├── image_downloader.py # Downloads book images
│
├── main.py                 # Entry point of the application
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored file


## Installation

### 1. Create the Repository using terminal

git create git@github.com:cannypeae/book-price-monitor.git
cd book-price-monitor

### 2. Create a Virtual Environment by running the following in terminal
python -m venv venv

### 3. Activate it by running Windows (PowerShell):**
venv\Scripts\activate

### 4. Install Dependencies using terminal
pip install -r requirements.txt

## ▶️ Usage
Run the program using terminal:
python main.py

This will:
* Scrape all book categories
* Extract each book’s details
* Download book images
* Save CSV files per category in `/data/`
* Store images in `/images/<category>/`

## 📊 Output Example

### CSV Files
data/travel.csv
data/mystery.csv

### Images
images/travel/a897fe39b1053632.jpg
images/mystery/b12cd45f6789012.jpg

## Notes
* Output folders (`data/`, `images/`) are excluded from Git
* Scraping includes a small delay to avoid overwhelming the server
* Designed for educational purposes only

## ETL Pipeline Explanation
This project demonstrates a simplified ETL pipeline:

1. **Extract** – Scrapes raw HTML data from the website
2. **Transform** – Cleans and structures data into consistent fields
3. **Load** – Saves structured data into CSV files and organizes images

This pipeline can be extended to:
* Run automatically on a schedule (daily monitoring)
* Store data in a database
* Track price changes over time
* Provide dashboards or APIs for analysis

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* Git & GitHub


## Author
Princewil Mbah


## License
This project is for educational and demonstration purposes.