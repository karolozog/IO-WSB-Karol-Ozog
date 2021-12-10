import pandas as pd
import matplotlib.pyplot as pyplot

tabela = pd.read_csv (r'miasta.csv')

rok_2010 = {'Rok':2010, 'Gdansk':460, 'Poznan':555, 'Szczecin':405}

df=tabela.append(rok_2010,verify_integrity=True, ignore_index=True)


pyplot.plot(df.Gdansk, marker = 'o', color = 'r')
pyplot.plot(df.Poznan, marker = 'o', color = 'y')
pyplot.plot(df.Szczecin, marker = 'o')
pyplot.ylabel("Liczba ludności w tys.")
pyplot.xlabel("Lata")
pyplot.title('Ludność w miastacg Polski')
pyplot.show()
print (df)