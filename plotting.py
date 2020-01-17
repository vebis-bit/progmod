from pylab import *

def f(x):
    return x**2

xverdier = []
yverdier = []

for x in range(-3,4):
    xverdier.append(x)
    yverdier.append(f(x))

print(xverdier,yverdier)

plot(xverdier,yverdier)
grid()
show()