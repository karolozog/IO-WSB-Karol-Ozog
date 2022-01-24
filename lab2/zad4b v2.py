import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("diabetes.csv")
zero_not_accepted = ["glucose-concentr","blood-pressure","skin-thickness","insulin","mass-index"]
score = ["class"]
for column in zero_not_accepted:
    dataset[column] = dataset[column].replace(0, np.NaN)
    mean = int(dataset[column].mean(skipna=True))
    dataset[column] = dataset[column].replace(np.NaN, mean)

for column in score:
    dataset[column] = dataset[column].replace("tested_positive", 1)
    dataset[column] = dataset[column].replace("tested_negative", 0)

#podział na dane szkoleniowe
X = dataset.iloc[:, 0:8]
y = dataset.iloc[:, 8]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.67)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=3, p=2, metric ="euclidean")

import math
math.sqrt(len(y_test))
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print("Macierz błędu")
print(cm)
print("dokładność przy kNN-3:")
k3 = accuracy_score(y_test, y_pred)
print(k3)

classifier5 = KNeighborsClassifier(n_neighbors=5, p=2, metric ="euclidean")
classifier5.fit(X_train,y_train)
y_pred5 = classifier5.predict(X_test)
cm5 = confusion_matrix(y_test, y_pred5)
print("Macierz błędu")
print(cm5)
print("dokładność przy kNN-5:")
k5 =accuracy_score(y_test, y_pred5)
print(k5)

classifier11 = KNeighborsClassifier(n_neighbors=11, p=2, metric ="euclidean")
classifier11.fit(X_train,y_train)
y_pred11 = classifier11.predict(X_test)
cm11 = confusion_matrix(y_test, y_pred11)
print("Macierz błędu")
print(cm11)
print("dokładność przy kNN-11:")
k11 =accuracy_score(y_test, y_pred11)
print(k11)

x = ["kNN-3", "kNN-5", "kNN-11"]
h = [k3, k5, k11]
c = ["red", "green", "blue"]
plt.bar(x,h, color =c )
plt.xlabel("klasyfikator")
plt.ylabel("dokładność klasyfikatora")
plt.title("Dokładność klasyfikatora - cukrzyca u kobiet w Ameryce")
plt.show()


