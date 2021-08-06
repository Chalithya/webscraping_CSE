from bs4 import BeautifulSoup
import requests
import pandas as pd


#getting teh html page from URL
url  ='https://yts.mx'

page = requests.get(url)

#print(page.status_code)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)
# print(soup.title)
testValue = soup.find('div', {'id':'popular-downloads'})


titles =[]

for i in testValue.find_all('a'):
    
    title = i.text
    titles.append(title)

print(titles)