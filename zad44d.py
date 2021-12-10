import pandas as pd
import matplotlib.pyplot as pyplot

tabela = pd.read_csv (r'miasta.csv')

rok_2010 = {'Rok':2010, 'Gdansk':460, 'Poznan':555, 'Szczecin':405}

df=tabela.append(rok_2010,verify_integrity=True, ignore_index=True)


pyplot.plot(df.Gdansk, marker = 'o', color = 'r', label = 'Gdańsk')
pyplot.plot(df.Poznan, marker = 'o', color = 'y', label = 'Poznań')
pyplot.plot(df.Szczecin, marker = 'o', label = 'Szczecin')
pyplot.ylabel("Liczba ludności w tys.")
pyplot.xlabel("Lata")
pyplot.title('Ludność w miastacg Polski')
pyplot.legend()
pyplot.show()
print (df)