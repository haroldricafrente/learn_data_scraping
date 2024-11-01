import pandas as pd
from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_Philippines'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
table = soup.find('table', class_ = 'wikitable sortable')
table = soup.find_all('table')[0]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles ]
df = pd.DataFrame(columns=world_table_titles)
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'D:\web scraping\lesson1_companies\bonus_companies.csv', index = False)