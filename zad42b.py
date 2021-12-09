a = int(input("podaj liczbę a:"))
b = int(input("podaj liczbę b:"))
c = int(input("podaj liczbę c:"))

def max_sum(a,b,c):
    if a >= b and c >= b:
        return(a + c)
    elif b >= a and c >= a:
        return(b +c)
    else:
        return(a + b)
max = max_sum(a, b, c)
print(max)


