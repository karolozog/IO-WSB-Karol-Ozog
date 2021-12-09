s = 0
p = 1
for i in range(2, 8, 2):
    s = s + i
    p = p * i
print(s)
print(p)

# zmienna s : program dodaje do siebie wartości i
# s = (s)0 + (i)2 => (s)2 +(i)4 => (s)6 + (i)6 =>  12

# zmienna p : program mnoży zmienną p * i
# p =(p)1 * (i)2 => (p)2 * (i)4 => (p)8 * (i)6 => 48 