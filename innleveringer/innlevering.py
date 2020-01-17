#innlevering med vurdering


#oppgave 1 kjemi
"""
import math

x = float(input("skriv inn konsentrasjonen av oksoniumioner i mol/L: "))

def pH(x):                      #deffinerer pH som en funksjon
    return -math.log(x, 10)     #setter inn formelen for pH
print(pH(x))                    #skriver ut pH verdi



#oppgave 2 biologi
from pylab import *

bakterier = 1000
CFU = []
tid = []
for i in range(0, 16):
    bakterier = bakterier*1.62
    print(i, "time(r) : ", bakterier)
    CFU.append(bakterier)
    tid.append(i)
print(CFU, tid)


for i in range(0, 16):
    bakterier = bakterier*1.62
    print(i, "time(r) : ", bakterier)
    
    CFU.append(bakterier)
    tid.append(i)
print(CFU, tid)

plot(tid, CFU)
title("Antall bakterier per time i CFU")
xlabel("Tid i Timer")
ylabel("Antall bakterier")
grid()
#vet ikke hvordan man gjør c oppgaven


#oppgave 3 fysikk


import math

v0 = 1
a = 1
t = 1

def v(a, t, v0):
    return v0 + a * t
print()
def s(v0, t, v):
    return 1/2 * (v0 + v) * t
print(s(a, t, v0))

def s2(t, a, v0):
    return v0 * t + 1/2 * a * t**2
print(s2(t, a, v0))

def v2(s, v0, a):
    v2 = v0**2 + 2 * a * s
    return sqrt(v2)
print(v2(t, v0, a))

"""

#oppgave 4 matte
def m(x, y, z):
    return(x**3 + y**3 + z**3)              #definerer formelen som en funksjon


k = 0                                       #lager en variabel for antall løsninger ligningen kan ha.

for n in range(0, 11, 1):                   #lager en løkke for n mellom 0 og 10
    for x in range(-100, 101, 1):           #lager en løkke for å sjekke løsninger for x innenfor 
        for y in range(-100, 101, 1):       #lager en løkke for å sjekke løsninger for y
            for z in range(-100, 101, 1):   #lager en løkke som sjekker alle z løsningene som passer med resten av likningen 
                if m(x, y, z) == n:         #hvis m = n vil programmet først telle det som en løsning og så skrive ut løsningen. kaller på funksjon for likning
                    k += 1
                    print("n:", n, " (", x, ",", y,",", z, ")")
    
print("antall løsninger der n er [0, 10] er:", k, "hvis x, y og z er [-100, 100] og alle tallene er heltall.")  #skriver ut svaret når regningen er ferdig.


