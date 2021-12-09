print("podaj długiość boku:")
bok = (int(input()))
poziom = bok * "x"


for i in range(bok):
    galaz = (bok - (bok -i))*"x"
    print(galaz)
print(poziom)