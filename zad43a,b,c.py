import numpy as np
x = np.array([3, 8, 9, 10, 12])
y = np.array([8, 7, 7, 5, 6])

suma = x + y
iloczyn = x * y
print("suma macierzy x + y to: ", suma)
print("iloczyn macierzy x * y to: ", iloczyn)

print("Iloczyn skalarny macierzy: ", np.dot(suma, iloczyn))

dist = np.sqrt(np.sum(np.square(x)))

print("Długość Eukialidesowa wektora x to: ", str(round(dist, 2)))