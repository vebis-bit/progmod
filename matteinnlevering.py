#oppgave 3 fysikk
from pylab import *

v0 = float(input("startfart(m/s): "))
a = float(input("akselerasjon(m/s^2): "))                         #definerer variablene 
t = float(input("tid(s): "))

def v1(a, t, v0):
    return v0 + a * t

def s(v0, t, v):
    return 1/2 * t * v0 + 1/2 * v1(a,t,v0) * t
                                                        #definerer formlene som funksjoner
def s2(t, a, v0):
    return v0 * t + 1/2 * a * t**2

def v2(s2, v0, a):
    v2 = v0**2 + 2 * a * s2(t,a,v0)
    return sqrt(v2)
print("")
print("Fartsformelen når startfart er",v0, "m/s, akselerasjon er", a, "m/s^2 og tid er", t, "s gir farten", v1(a, t, v0), "m/s.")
print("")
print("Første strekningsformel når farten er", v1(a,t,v0), "m/s, tiden er", t, "s og startfarten er", v0, "m/s gir strekning", s(a, t, v0), "m.")
print("")
print("Den andre strekningsformelen, gir", s2(t, a, v0), "m, hvis tiden er", t, "s, akselerasjonen er", a, "m/s^2 og startfarten er", v0, "m/s.")
print("")
print("Den tidløse formelen gir", v2(s2, v0, a), "m/s, hvis strekningen er", s2(t,a,v0), "m, startfarten er", v0, "m/s og akselerasjonen er", a, "m/s^2")
