print("podaj imiona rozdzielone przecinkami")
imiona = input()
tablica = imiona.split()

for i in range (len(tablica)):
    imie = tablica[i]
    if (imie.endswith("a")) or (imie.endswith("a,")):
     print(imie)
     imie = tablica[0 + i]
     
