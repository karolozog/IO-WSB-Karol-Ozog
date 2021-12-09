a = 1
i = 0
tablica = []

while i < 20:
    if a % 2 != 0:
            tablica.append(a)
            a +=2
    i +=1
  
print(sum(tablica))