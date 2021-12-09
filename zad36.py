print("Podaj boki prostokąta a i b oddzielone spacją")
boki = input()
booki = boki.split()
a = int(booki[0])
b = int(booki[1])

if (a <= 0) or (b <= 0):
     print("nieprawidłowe dane")
else:
    p = a * b
    L = 2*a + 2*b
    print("Pole prostokąta p=", p, "a obwód L =", L)
  