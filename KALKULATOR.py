print(" __________________")
print("|                  |")
print("|    KALKULATOR    |")
print("|                  |")
print("|     v.1.0.0      |")
print("|__________________|")

import logging
logging.basicConfig(level=logging.DEBUG)


operation=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
a=float(input("Podaj pierwszą liczbę: "))
b=float(input("Podaj drugą liczbę: "))

def calc(a,b):
    if operation == '1':
        suma = (a+b)
        logging.debug("Dodaję %d i %d" %(a,b)) 
        print(f"Wynik to {suma}")
    elif operation == '2':
        różnica=(a-b)
        logging.debug("Odejmuję %d od %d" %(b,a))
        print(f"Wynik to {różnica}")
    elif operation == '3':
        iloczyn=(a*b)
        logging.debug("Mnożę %d razy %d" %(a,b))
        print(f"Wynik to {iloczyn}")
    elif operation == '4':
        if b==0:
            print("Nie dziel przez zero")
        if a==0:
            print("Nie dzielimy zera")
        else:
            iloraz=(a/b)
            logging.debug("Dzielę %d przez %d" %(a,b))
            print(f"Wynik to {iloraz}")
    else:
        print("Błąd. Podano złe wartości")
calc(a,b)






    