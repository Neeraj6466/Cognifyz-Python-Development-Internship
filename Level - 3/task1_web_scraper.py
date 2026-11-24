
# Cognifyz Internship
# Level 3 - Task 1
# Web Scraper

import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://books.toscrape.com/"

# Get website data
response = requests.get(url, timeout=10)

# Check website response
response.raise_for_status()

# Read HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

print("===== BOOK DETAILS =====")

# Extract book names and prices
for book in books:

    title = book.find("h3").find("a")["title"]

    price = book.find("p", class_="price_color").text

    print("Book Name:", title)
    print("Price:", price)
    print("----------------------")
