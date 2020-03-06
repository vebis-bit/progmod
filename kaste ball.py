from pylab import *

# Konstanter
k = 0.3 # Luftmotstand
g = -9.81 # Tyngdeakselerasjon i m/s^2 
m = 1 # Masse i kg
v0 = 80 # Starthastighet i m/s
s0 = 0 # Startposisjon i m

# Tidsvariabler
dt = 0.005 # Tidsintervall i s
tid_start = 0
tid_slutt = 10
N = int((tid_slutt-tid_start)/dt) # Antall intervaller

# Arrayer
t = zeros(N+1)
a = zeros(N+1)
v = zeros(N+1)
s = zeros(N+1)

# Startverdier
t[0] = tid_start 
v[0] = v0
s[0] = s0

for i in range(N):
    a[i] = g - k*v[i]/m
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = s[i] + v[i]*dt + 0.5*a[i]*dt**2 
    t[i+1] = t[i] + dt




plot(t,s, label='Strekning (m)')
title("Fallende ball")
xlabel("Tid (s)")
ylabel("Y-aksen")
plot(t, a, label='Akselerasjon (m/s^2)')
plot(t, v, label='Fart (m/s)')
legend()
show()