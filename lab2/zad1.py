import pandas as pd

df = pd.read_csv("iris.csv")
print(df)

def myPredictRow(sl, sw, pl, pw):
    if pl < 2:
        return "Setosa"
    else:
        if pw < 1.8:
            return "Versicolor"
        else:
            return "Virginica"
def myPredict():
    zgodnosc = 0
    for i in range(0, 149):
        if myPredictRow(df["sepal.length"][i], df["sepal.width"][i], df["petal.length"][i], df["petal.width"][i]) == df["variety"][i]:
            zgodnosc += 1
    print('Zgodnosc: ', zgodnosc/150)

myPredict()
