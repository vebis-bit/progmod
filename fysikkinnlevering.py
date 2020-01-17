#oppgave 1 kjemi
import math

x = float(input("skriv inn konsentrasjonen av oksoniumioner i mol/L: "))

def pH(x):                      #deffinerer pH som en funksjon
    return -math.log(x, 10)     #setter inn formelen for pH
print(pH(x))                    #skriver ut pH verdi

