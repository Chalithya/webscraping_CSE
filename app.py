# from typing import Text
from bs4 import BeautifulSoup
import requests
# import pandas as pd
# from requests.models import Response


#getting teh html page from URL
url  ='https://www.cse.lk/pages/trade-summary/trade-summary.component.html'

page = requests.get(url)
#print(page.status_code)

soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

# testValue = soup.find(id='1b')
# print(testValue)
print(soup.title.text)

# table = soup.find('table', {'id':'DataTables_Table_0'})
table = soup.find('table')
divVal = soup.find('div')
# vals = soup.find('div', {'class':'top'})
# print(divVal)
headers =[]

for i in divVal.find_all('table'):
    
    title = i.text
    headers.append(title)


print(headers)





#################################################### some other way ############################

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

