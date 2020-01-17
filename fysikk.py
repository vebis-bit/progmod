from pylab import *
valg = input("skriv her hvilke formel du vil bruke, bruk fart, tidløs, vei og akselerasjon som betegnelse: ")

def s1(t, a, v0):
    return 0.5*a*t**2+v0*t
def v1(t, a, v0):
    return a*t+v0 
def a1(t, v, v0):
    return (v-v0)/t
def v2(v0, a, s):
    return sqrt(v0**2+2*a*s)

if valg == "fart":
    t = float(input("tid: "))
    a = float(input("akselerasjon: "))
    v0 = float(input("startfart: "))
    print(v1(t, a, v0),"m/s")
if valg == "vei":
    t = float(input("tid: "))
    a = float(input("akselerasjon: "))
    v0 = float(input("startfart: "))
    print(s1(t, a, v0),"m")
if valg == "akselerasjon":    
    v = float(input("fart: "))
    t = float(input("tid: "))
    v0 = float(input("startfart: "))
    print(a1(t, v, v0),"m/s^2")
if valg == "tidløs":
    s = float(input("strekning: "))
    a = float(input("akselerasjon: "))
    v0 = float(input("startfart: "))
    print(v2(t, a, v0),"m/s")
