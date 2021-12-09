import string    
import random 
print("podaj liczbę dodatnią:") 
losowe = (int(input()))
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = losowe))    
print("Wygenerowany string to : " + str(ran)) 