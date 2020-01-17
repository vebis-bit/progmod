#oppgave 2 biologi
from pylab import *

bakterier = 1000
CFU = []                                #lager liste for CFU koloni og tid
tid = []
for i in range(0, 16):
    bakterier = bakterier*1.62          #bruker formelen for endring over tid
    print(i, "time(r) : ", bakterier)   #printer for å sjekke om alle verdiene er riktige
    CFU.append(bakterier)               #legger til hver enkelt verdi for bakterier og tid
    tid.append(i)

print(CFU, tid)                         #printer listene

bakterier2 = 1000                       
CFu2 = []                               #lager liste for CFU koloni og tid med begrensing
tid2 = []
for i in range(0, 16):
    bakterier2 = bakterier2*1.62
    print(i, "time(r) : ", bakterier2)
    if bakterier2/500 >= 1500:          #hvis det er flere enn 1500 bakterier per Ml i løsningen vil ifløkken kjøre og begrense veksten
        bakterier2 = 1500*500           #passer på at bakteriene ikke overskrider en hvis sum
    CFu2.append(bakterier2)             #legger hver enkelt verdi med begrensning inn i listen
    tid2.append(i)

print(CFu2, tid2)

plot(tid, CFU)
plot(tid2,CFu2)                             #skriver ut de to tabellene
title("Antall bakterier per time i CFU")    #grafikk
xlabel("Tid i Timer")
ylabel("Antall bakterier")
grid()

