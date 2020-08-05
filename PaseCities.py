# importing the libraries
from bs4 import BeautifulSoup
import requests

url="https://wordstat.yandex.ru/#!/history?period=weekly&regions=225"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, features="html.parser")
#print(soup.prettify()) # print the parsed data of html
print(soup.title.text)