#oppgave 4 matte
def m(x, y, z):
    return(x**3 + y**3 + z**3)              #definerer formelen som en funksjon

k = 0                                       #lager en variabel for antall løsninger ligningen kan ha.
l = k
for n in range(0, 11):                   #lager en løkke for n mellom 0 og 10
    for x in range(-100, 101):           #lager en løkke for å sjekke løsninger for x innenfor 
        for y in range(-100, 101):       #lager en løkke for å sjekke løsninger for y
            for z in range(-100, 101):   #lager en løkke som sjekker alle z løsningene som passer med resten av likningen 
                if m(x, y, z) == n:      #hvis m = n vil programmet først telle det som en løsning og så skrive ut løsningen. kaller på funksjon for likning
                    k += 1
                    print("n:", n, " (", x, ",", y,",", z, ")")
                       
print("antall løsninger der n er [0, 10] er:", k, "hvis x, y og z er [-100, 100] og alle tallene er heltall.")  #skriver ut svaret når regningen er ferdig.


