waga = 75
wzrost = 180

#sposob przez format
s = "Jan Kowalski (waga: {}, wzrost: {})"
s = s.format(waga, wzrost)
print(s)

#sposób przez konwersjé liczby na stringi 
waga_txt = str(waga)
wzrost_txt = str(wzrost)
s = "Jan Kowalski (waga: " + waga_txt + ", wzrost: " + wzrost_txt + ")"
print(s)

# TAK, jeśli stringi mają wartość liczb całkowitych
waga_int = int(waga_txt)
wzrost_int = int(wzrost_txt)
print(waga_txt)
print(wzrost_int)