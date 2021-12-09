x = 19

for i in range(2, x):
    if x % 2 == 0:
        print(x, "nie jest liczbą pirwszą")
        break
    else:
        print(x, "jest liczbą pierwszą")
        break