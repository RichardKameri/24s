import requests
from bs4 import BeautifulSoup
# Loop through the pages
page = 1
while True:
    response = requests.get(f"https://quotes.toscrape.com/page/{page}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.select('.quote')
        if not quotes:
            break
        for quote in quotes:
            text = quote.select_one('.text').get_text()
            author = quote.select_one('.author').get_text()
            print(f"Quote: {text}\nAuthor: {author}\n")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    page += 1







