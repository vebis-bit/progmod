from pylab import*
"""
navn = ["andreas with a diamond hoe", "magnus", "magnus"]
tall = [5, 2, 2, 2]

print(tall)
# .append legger til i en liste
tall.append(113)
print(tall)

partall = []

for hoe in range(0, 10001, 2):
    partall.append(hoe)
    
partall.remove(42) # .remove tar vekke t tall fra en liste
    
print(partall)


def f(x):
    return x**3 - 2*x

x = []
for i in range(-50, 51):
    x.append(i)

x = array(x)
y = f(x)


plot(x, y)
"""

film = ["game of thrones", "greys anathomy", "white colar", "vikingane"]

film.append("rick and morty")

film.remove("vikingane")

print(film)

liste = ["menneske", "nebbdyr", "skilpadde", "maursluker", "sjøpølse", "sjøoter"]

liste.pop(3)

print(liste[:3])    # skriver ut alle tallene til indeks tall 3 i liste
print(liste[3:])    # skriver ut alle tallene fra og med index tall 3
print(liste[3])     # skriver ut tallet som er nummer tre i rekken
