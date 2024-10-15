import requests
from bs4 import BeautifulSoup
import csv
base_url = 'https://quotes.toscrape.com/page/{}'
# Open CSV file for writing
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])
    # Loop through the pages
    page = 1
    while True:
        url = base_url.format(page)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.select('.quote')
            if not quotes:
                break
            for quote in quotes:
                text = quote.select_one('.text').get_text()
                author = quote.select_one('.author').get_text()
                writer.writerow([text, author])
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
        page += 1
print('All quotes have been saved to quotes.csv')