print("podaj długiość boku:")
bok = (int(input()))
poziom = bok * "x"



for i in range(bok):
    galaz = (bok - (bok -i))*"x"
    spacje = (bok - i)*" "
    print(spacje+galaz)
print(poziom)
  
