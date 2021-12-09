import numpy as np
x = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
y = np.array([[1, 2, 1],[2, 4, 6],[7, 2, 5]])

iloczyn = np.dot(x,y)
print("wynik mnożenia macierzowego to: ",iloczyn)