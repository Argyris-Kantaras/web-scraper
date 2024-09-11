from turtle import title
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


results = list([])

# load html
page = urllib.request.urlopen(
    "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=lights&_sacat=0&_odkw=batteries&_osacat=0.html")
soup = bs(page)

my_titles = soup.body.find_all('div', {"class": "s-item__title"})

titles = []
for i in my_titles:
    i = i.text
    titles.append(i)
titles = titles[1:]
# Prices
my_prices = soup.body.find_all('span', {"class": "s-item__price"})
prices = []

for i in my_prices:
    i = i.text
    prices.append(i)
prices = prices[1:]
data = pd.DataFrame({'titles': titles, 'prices': prices})
data.to_csv('D:\python projects\web scraping\price_list.csv')
print(data)
