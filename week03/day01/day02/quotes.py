import requests
from bs4 import BeautifulSoup
# Loop through the pages
page = 1
while True:
    response = requests.get(f"https://quotes.toscrape.com/page/{page}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.findAll('div', class_='quote')
        if not quotes:
            break
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            print(f"Quote: {text}\nAuthor: {author}\n")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    page += 1