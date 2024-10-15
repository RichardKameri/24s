import requests
from bs4 import BeautifulSoup

# Base URL of the site
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Function to extract book details from a page
def extract_books_from_page(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    book_details = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.p["class"][1]
        book_details.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })
    
    return book_details

# Main function to scrape books from all pages
def scrape_all_books():
    all_books = []
    page = 1

    while True:
        page_url = base_url.format(page)
        books = extract_books_from_page(page_url)
        
        if not books:
            break

        all_books.extend(books)
        page += 1

    return all_books

# Scrape books and print the results
all_books = scrape_all_books()
for book in all_books:
    print(f"Title: {book['title']}, Price: {book['price']}, Availability: {book['availability']}, Rating: {book['rating']}")
