!wget https://raw.githubusercontent.com/iqbalhanif/Sanberlearn/master/INDODAPOERData.csv

import pandas as pd

df = pd.read_csv('INDODAPOERData.csv')
col_name = ['Country Name',
 'Country Code',
 'Indicator Name',
 'Indicator Code',
 '2001',
 '2002',
 '2003',
 '2004',
 '2005',
 '2006',
 '2007',
 '2008',
 '2009',
 '2010',
 '2011',
]
city_name = ["Bandung, Kota", "Bandung Barat, Kab.", "Bandung, Kab.", "Cimahi, Kota"]
df2 = df[col_name]
df2 = df2[df2['Country Name'].isin(city_name)]
df2 = df2[df2['Indicator Name'] == 'Total GDP excluding Oil and Gas (in IDR Million), Current Price']

df3 = df2.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
df3.set_index(['Country Name'], inplace=True)
df4 = df3.stack()

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.plot(df4['Bandung Barat, Kab.'], label = 'Kab. Bandung Barat')
plt.plot(df4['Bandung, Kota'], label = 'Kota Bandung')
plt.plot(df4['Bandung, Kab.'], label = 'Kab. Bandung')
plt.plot(df4['Cimahi, Kota'], label = 'Kota Cimahi')
plt.ylabel('GDP (In Million Rupiahs')
plt.xlabel('Year')
plt.ticklabel_format(style='sci', axis='y', scilimits=(-1000000,1000000))
plt.legend(loc="upper left")
plt.show()
