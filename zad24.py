tablica = [5, 10, 15, 20, 25, 30]
tablica.append(35)

#odwrócona tablica
tablica.reverse()
print(tablica)

#usunięcie śreodkowego elementu
tablica.reverse()
tablica.remove(20)
print(tablica)

#wyświetlenie maksymalnej liczby z listy
print(max(tablica))

#suma liczb w liście
print(sum(tablica))

#średnia liczb z listy
print(sum(tablica) / len(tablica))