from bs4 import BeautifulSoup
import requests
import pandas as pd


#getting teh html page from URL
url  ='https://www.aliexpress.com/item/32585047296.html?spm=a2g0o.ams_97944.topranking.1.2caa83ew83ewvv&pdp_ext_f=%7B%22ship_from%22:%22AU%22,%22sku_id%22:%2212000016020066548%22%7D&scm=1007.26694.226824.0&scm_id=1007.26694.226824.0&scm-url=1007.26694.226824.0&pvid=25faf535-59e5-453c-b3a2-5f273513a2c7&fromRankId=1773985&_t=fromRankId:1773985'

page = requests.get(url)

#print(page.status_code)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

testValue = soup.find_all("div", {'class':'product-price-current'})
print(testValue)
# print(soup.title.text)