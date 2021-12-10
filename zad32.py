x = int(input("podaj liczbę: "))

for i in range(2, x):
    if x % i == 0:
        print(x, "nie jest liczbą pierwszą")
        break
    else:
        print(x, "jest liczbą pierwszą")
        break