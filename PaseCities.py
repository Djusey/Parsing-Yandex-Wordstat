# importing the libraries
from bs4 import BeautifulSoup
import requests
import io
#url="file:///C:/Users/Djusey/PycharmProjects/ParsingYandexWordstat/Parsing%20Yandex%20Wordstat/CitiesFrame.html"

# Make a GET request to fetch the raw HTML content
#html_content = requests.get(url).text
filecities = io.open("CitiesFrame.txt", encoding='utf-8')
# Parse the html content
soup = BeautifulSoup(filecities, features="lxml")
print(soup.prettify()) # print the parsed data of html
#print(soup.title.text)

# import pandas as pd
#
# tables = pd.read_html("CitiesFrame.html")
# print(tables[0])