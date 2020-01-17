from pylab import *

def f(x):
    return x**2

x_liste = []
y_liste = []

for x in range(-3,4):
    x_liste.append(x)
    y_liste.append(f(x))
    
plot(x_liste, y_liste)
show()
print("Hei på du!")

