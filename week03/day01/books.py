# import requests
# from bs4 import BeautifulSoup

# # URL to scrape
# url = "http://books.toscrape.com/"

# # Send a GET request to the webpage
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all the book sections
# books = soup.find_all("article", class_="product_pod")

# # Loop through each book and extract the title and price
# for book in books:
#     # Extract the title
#     title = book.h3.a["title"]

#     # Extract the price
#     price = book.find(class_="price_color").text

#     print(f"Title: {title}, Price: {price}")

import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://books.toscrape.com/"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the book sections
books = soup.find_all("article", class_="product_pod")

# Loop through each book and extract availability and rating
for book in books:
    # Extract the title
    title = book.h3.a["title"]
    
    # Extract the availability
    availability = book.find("p", class_="instock availability").text.strip()
    
    # Extract the rating
    rating = book.p["class"][1]
    
    print(f"Title: {title}, Availability: {availability}, Rating: {rating}")

