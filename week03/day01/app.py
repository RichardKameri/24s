import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

if response.status_code == 200:
   soup = BeautifulSoup(response.text, 'html.parser')
   quotes = soup.findAll('div', class_ = "quote")
   print(quotes)

   for quote in quotes:
      text = quote.find('span', class_ ='text').get_text()
      author = quote.find('small', class_= 'author').get_text()
      print(f"quote: {text}\nAuthor:{author}\n")

else:
   print(f"failed to retreive the page. Status code: {response.status_code} ")
