from pylab import *

B = 2*10**9
k = 0.3+1
startsum = 10000            #definerer variabler
sluttsum = 10000
tid = 0

tidliste = []
bakterieliste = []          #definerer tomme lister


for tid in range(61):                #for løkke frem til og med 60
    sluttsum *= k
    tidliste.append(tid)
    bakterieliste.append(sluttsum)

print(tidliste, bakterieliste)       #printer ut listene

plot(tidliste, bakterieliste)
ylabel("Antall bakterier i kolonien (ganget med 10^10)")
xlabel("Tid i minutter")
grid()
title("Tidvis vekst i e.coli-bakteriekolonini en petriskål.")