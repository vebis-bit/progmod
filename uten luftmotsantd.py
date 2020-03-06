from pylab import *

#konstanter
k = 0.3     # luftmotstand
g = -9.81   # tyngdens akselerasjon i m/s^2
m = 1       # vekt i kg
v0 = 25     # startfart i m/s
s0 = 0      # startposisjon i m

# Tidsvariabler
dt = 0.0005     # tidsintrvall i sekunder
tid_start = 0
tid_slutt = 5
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
