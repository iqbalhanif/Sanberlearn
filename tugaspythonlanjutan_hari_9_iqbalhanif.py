
import csv
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd
import numpy as np

alamat = "https://pokemondb.net/pokedex/all"
safeAdd = Request(alamat, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(safeAdd)
data = bs(html, 'html.parser')

table = data.find("table", {"id":"pokedex"})
rows = data.findAll("tr")

row_data = []
for row in rows:
    cell_data = []

    if row.contents[1].get_text() == "501": #stop function
        break

    for item in row.findAll(["th","td"]): #gathering function
        cell_data.append(item.get_text())
    row_data.append(cell_data)

df = pd.DataFrame(row_data)
df.columns = df.iloc[0]
df = df[1:]
df.to_csv('data_pokemon.csv',index=False)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.read_csv("data_pokemon.csv") 

data["Attack"] = pd.to_numeric(data["Attack"])
data["Defense"] = pd.to_numeric(data["Defense"])

#menambahkan dua kolom tranformasi
data["Alog"] = np.log(data["Attack"])
data["Dlog"] = np.log(data["Defense"])

log_data = data.iloc[:, 10:12]
log_array = np.array(log_data)

kmeans = KMeans(n_clusters=3, random_state=200)
kmeans.fit(log_array)
data['kluster'] = kmeans.labels_

plt.scatter(data.Attack, data.Defense, s = 20, c = data.kluster, marker = "o", alpha = 0.5)
plt.title("Hasil Klustering K-Means")
plt.xlabel("Atk")
plt.ylabel("Def")
plt.show()

sse = []
k_list = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters = k).fit(log_data)
    centroids = kmeans.cluster_centers_
    prediksi = kmeans.predict(log_array)
    nilai_sse = 0
    
    for i in range(len(log_array)):
        titik_pusat = centroids[prediksi[i]]
        nilai_sse += (log_array[i, 0] - titik_pusat[0]) ** 2 + (log_array[i, 1] - titik_pusat[1]) ** 2
    
    sse.append(nilai_sse)
    k_list.append(k)

plt.plot(k_list,sse)
plt.show()

from sklearn.metrics import silhouette_score

daftar = []
k_list = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters = k).fit(log_array)
    labels = kmeans.labels_
    daftar.append(silhouette_score(log_array, labels, metric = 'euclidean'))
    k_list.append(k)

plt.plot(k_list,daftar)
plt.show()

kmeans = KMeans(n_clusters=2, random_state=200)
kmeans.fit(log_array)
data['kluster'] = kmeans.labels_

data.to_csv('data_cluster.csv',index=False)
print("Jumlah K terbaik adalah K=2")
