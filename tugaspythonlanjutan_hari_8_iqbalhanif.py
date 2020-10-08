import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

table = soup.find('table',{'class':'wikitable sortable'}).tbody
rows = table.find_all('tr')
columns = [v.text.replace('\n','') for v in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

for i in range(2,len(rows)):
    tds = rows[i].find_all('td')
    values = [td.text.replace('\n',''.replace('\xa0','')) for td in tds]

    df = df.append(pd.Series(values, index=columns), ignore_index=True)
    #print(df)

df.to_csv("namefile.csv")

# buat barchart
from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference
import csv

#inisiasi excel
wb = Workbook()
ws = wb.active

#open file
data = open('namefile.csv')
rows = csv.reader(data, delimiter=',')

index = 0
for row in rows:
    data_clean = []
    for i in row:
        try:
            i = float(i)
        except:
            pass
        data_clean.append(i)
    ws.append(data_clean)
    index +=1
len_row = len(data_clean)
wb.save("iqbalhanifipb.xlsx")