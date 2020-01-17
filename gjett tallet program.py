from pylab import *


tall = 0
randtall = randint(1,101)
forsok = 0

while tall != randtall:
    tall = int(input("hvilke tall mellom 1 og 100 tenker jeg på? "))
    forsok += 1
    if tall < randtall:
        print("Du gjetter litt for lavt")
    elif tall > randtall:
        print("du gjetter litt høy")
print("eyyyy du gjettet riktig på", forsok, "forsøk")