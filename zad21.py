a = 1
b = 3
c = 3
if a == b:
    if b == c:
        print("Wszytskie liczby a, b i c sa sobie równe")
    else:
         print("liczby a i b są sobie równe")
elif b == c:
    if a == c:
        print("Wszytskie liczby a, b i c sa sobie równe")
    else:
        print("Liczby b i c sa sobie równe")
elif a == c:
    if b == c:
        print("Wszytskie liczby a, b i c sa sobie równe")
    else:
         print("Liczby a i c są sobie równe")
else:
     print("Nie ma pary równych liczb")
   