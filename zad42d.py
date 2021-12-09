a = int(input("podaj podstawę trapezu a:"))
b = int(input("podaj podstawę trapezu b:"))
h = int(input("podaj wysokość trapezu h:"))

def pole_trapezu(a, b, h):
    pole = ((a +b) * h)/2
    print(pole)

pole_trapezu(a, b, h)