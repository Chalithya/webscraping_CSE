from bs4 import BeautifulSoup
import requests
import pandas as pd
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='Name of the CSV file') 
    args_values = parser.parse_args()
   
    table_values = reading_table()
    printing_table(table_values, args_values.name)
        



def reading_table():
    #getting teh html page from URL
    url  ='https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    header_values : str = []
    table = soup.find('table')
    headers = table.find_all('th')

    for header in headers:   
        title = header.text.strip()
        header_values.append(title)

    #creating a data frame to keep the values
    df = pd.DataFrame(columns=header_values)
    rows = table.find_all('tr')

    for row in rows[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
    
    return df
    
   


def printing_table(df, name : str):
    df.to_csv('{}.csv'.format(name))
    print('{} Document created'.format(name))




if __name__ == '__main__':
    main()


