from bs4 import BeautifulSoup
import requests

# Creates a header
headers = {'User-agent': 'Mozilla/5.0'}

# Requests the webpage
request = requests.get('https://www.vg.no/nyheter/', headers=headers)
html = request.content


soup = BeautifulSoup(html, 'html.parser')
aa = input("Skriv inn et tall fra 1-38: ")
titles = soup.find_all('h3')
parent = titles[int(aa)]
print(parent)
