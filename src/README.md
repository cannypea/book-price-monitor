```markdown
#  Book Price Monitoring System

This project is a Python-based web scraping application that extracts book data from
Books to Scrape. It is designed as a beta version of a price monitoring system for an online bookstore.

##  Overview

The application:
- Scrapes book data from all categories
- Extracts detailed product information
- Saves structured data into CSV files
- Downloads and organizes book images

##  Features

The scraper collects the following data for each book:
- Product page URL  
- Universal Product Code (UPC)  
- Book title  
- Price (including and excluding tax)  
- Quantity available  
- Product description  
- Category  
- Review rating  
- Image URL  


##  Project Structure

```bash

book-price-monitor/
│
├── src/
│   ├── scraper.py
│   ├── category_scraper.py
│   ├── site_scraper.py
│   ├── image_downloader.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore

````

##  Installation

### 1. Clone the Repository

```bash
git clone git@github.com:cannypea/book-price-monitor.git
cd book-price-monitor
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows (PowerShell):**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Run the Project

Run the main script:

```bash
python main.py
```

##  Output

After running the script, the following will be generated:

### 1. CSV Files

* Located in the `data/` folder
* One CSV file per category

Example:

```
data/travel.csv
data/mystery.csv
```

### 2. Images

* Stored in the `images/` folder
* Organized by category
* Named using the book’s UPC

Example:

```
images/travel/a897fe39b1053632.jpg
```

##  Important Notes

* The `data/` and `images/` folders are not included in the repository
* These files are generated when the script is executed
* Ensure you have an active internet connection before running the scraper;

##  How It Works (ETL Overview)

* **Extract**: Scrapes raw HTML data from the website
* **Transform**: Cleans and structures the data into consistent fields
* **Load**: Saves the data into CSV files and downloads images

##  Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

##  Author

Princewil Mbah