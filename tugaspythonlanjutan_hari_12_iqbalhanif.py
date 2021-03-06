# -*- coding: utf-8 -*-
"""TugasPythonLanjutan_Hari_12_IqbalHanif.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G2Tpvu7eij6OCjAEGakfpHZXmjqRGzU8
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

!wget https://raw.githubusercontent.com/iqbalhanif/Sanberlearn/master/response.json
!wget https://raw.githubusercontent.com/iqbalhanif/Sanberlearn/master/response2.json
!wget https://raw.githubusercontent.com/iqbalhanif/Sanberlearn/master/response3.json

df_indo = pd.read_json('response.json')
df_korea = pd.read_json('response2.json')
df_vietnam = pd.read_json('response3.json')
df_korea.head()

frames = [df_indo, df_korea, df_vietnam]
df = pd.concat(frames)
df['Country'].unique()

fig = plt.figure(figsize=(15,15))
ax = plt.axes()

case1 = df_indo['Cases'].to_numpy()
date1 = df_indo['Date'].to_numpy()
case2 = df_korea['Cases'].to_numpy()
date2 = df_korea['Date'].to_numpy()
case3 = df_vietnam['Cases'].to_numpy()
date3 = df_vietnam['Date'].to_numpy()


plt.plot(date1, case1, color='blue', label ='Indonesia') 
plt.plot(date2, case2, color='green', label = 'South Korea')    
plt.plot(date3, case3, color='red', label = 'Vietnam') 
plt.title("Total Confirmed Cases in 3 country")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend();

"""Analisis:
Confirmed cases di Indonesia masih bertumbuh cukup signifikian mengikuti sebaran eksponensial, sedangkan pertumbuhan confirmed cases di Vietnam dan Korea Selatan sudah mulai stagnan (kurva cenderung mendatar). Ini menunjukkan bhawa penanganan COVID-19 di Korea dan Vietnam jauh lebih baik daripada Indonesia
"""