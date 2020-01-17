from pylab import *

c = 3.0*10**8
h = 6.63*10**(-34)
B = 2.18*10**(-18)

def deeksitasjon_av_skall(m,n):
    return c/((B/h)*((1/m**2)-(1/n**2)))


print("bølgelengden er,",deeksitasjon_av_skall(2,5)/10**(-9), "nm")

