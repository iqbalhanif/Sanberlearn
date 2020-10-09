!wget 'https://raw.githubusercontent.com/iqbalhanif/Sanberlearn/master/pulsar_stars.csv'

import seaborn as sn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix

dataset = pd.read_csv ('pulsar_stars.csv')
set_data = dataset.iloc [:, 1:8]
kluster_data = dataset.iloc [:,8]

x_train, x_test, y_train, y_test = train_test_split(set_data, kluster_data, test_size=0.25,random_state=150) # 75% training and 25% test

model_s = svm.SVC(kernel='linear') # Linear Kernel
model_s.fit(x_train, y_train)
y_pred = model_s.predict(x_test)
print(classification_report(y_test, y_pred))

disp = plot_confusion_matrix(model_s, x_test, y_test,
                             cmap=plt.cm.Blues,
                             )
print(disp.confusion_matrix)

model_k = KNeighborsClassifier(n_neighbors=1)
model_k.fit(x_train, y_train)
y_pred = model_k.predict(x_test)
print(classification_report(y_test, y_pred))

disp2 = plot_confusion_matrix(model_k, x_test, y_test,
                             cmap=plt.cm.Blues,
                             )
print(disp2.confusion_matrix)

error = []
for i in range(1, 50):
    model_k = KNeighborsClassifier(n_neighbors=i)
    model_k.fit(x_train, y_train)
    y_pred = model_k.predict(x_test)
    error.append(np.mean(y_pred != y_test))

plt.figure(1)  
plt.plot(range(1, 50), error, color='red', marker='o', markersize=5)
plt.title('Error pada nilai K')  
plt.xlabel('K')  
plt.ylabel('Error rata-rata')
plt.show()

model_k = KNeighborsClassifier(n_neighbors=5)
model_k.fit(x_train, y_train)
y_pred = model_k.predict(x_test)
print(classification_report(y_test, y_pred))

disp2 = plot_confusion_matrix(model_k, x_test, y_test,
                             cmap=plt.cm.Blues,
                             )
print(disp2.confusion_matrix)

print("K terbaik adalah k=5 dengan nilai error=", error[4])