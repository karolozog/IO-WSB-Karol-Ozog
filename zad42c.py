liczby = [56, 2, 3, 5, 6]

def wybierz_parzyste(x):
   for i in range (len(liczby)):
      if liczby[i] % 2 == 0:
         print(liczby[i])
         i += 1

wybierz_parzyste(liczby)