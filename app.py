from typing import Text
from bs4 import BeautifulSoup
import requests
import pandas as pd


#getting teh html page from URL
url  ='https://www.cse.lk/pages/trade-summary/trade-summary.component.html'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

print(soup.title.text)

table = soup.find('table', {'id':'DataTables_Table_0'})
# table = soup.find('table', {'class':'dataTable'})

headers =[]

for i in table.find_all('th'):
    
    title = i.text
    headers.append(title)

# data_table = soup.find('table', attrs={'id':'DataTables_Table_0'})
# data_table_body = data_table.find('thead') 
# headers = []
# rows = data_table_body.find_all('tr')

# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     headers.append([ele for ele in cols if ele])

# # for th in data_table.find_all('th'):
# #     title = th.text.strip()
# #     headers.append(title)
# print(headers)

