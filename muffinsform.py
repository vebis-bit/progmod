from pylab import *

#konstanter
k = 1       # sluttmotstand
g = 9.81    # tyngdens akselerasjon i m/s^2
m = 0.001   # vekt i kg
v0 = 0      # startfart i m/s
s0 = 0      # startposisjon i m

# Tidsvariabler
dt = 0.5     # tidsintrvall i sekunder
tid_start = 0
tid_slutt = 4
N = int((tid_slutt - tid_start)/dt) # antall intervaller 

#arrayer
t = zeros(N+1)
a = zeros(N+1)
v = zeros(N+1)
s = zeros(N+1)


#startverdier
t[0] = tid_start
v[0] = v0
s[0] = s0

for i in range(N):
    a[i] = g - k*v[i]**2/m
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = v[i+1]*dt + 0.5*a[i]**2
    t[i+1] = t[i] + dt


