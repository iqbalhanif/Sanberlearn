from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests

alamat = "https://www.kompas.com/"
html = requests.get(alamat)
data = BeautifulSoup(html.content, 'lxml')

items = data.find_all("h4", {"class":"most__title"})
teks = [p.get_text() for p in items]
df = pd.DataFrame(teks, columns = ['Judul Artikel'])
df