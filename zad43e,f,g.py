import numpy as np

wektor = np.random.randint(100, size=(50))

srednia = np.average(wektor)
minimalna = np.min(wektor)
maksymalna = np.max(wektor)
odchylenie = np.std(wektor)
zi=(srednia-minimalna)/(maksymalna-minimalna)

print(wektor)
print("średnia liczba całkowita to: ", int(srednia))
print("najmniejsza liczba to: ",minimalna)
print("największa liczba to: ",maksymalna)
print("odchylenie standardowe wynosi: ", int(odchylenie))
print("zi = ", zi)