from pylab import *

p0 = 1000
k = 0.62
B = 1000



# Tidsvariabler
dt = 0.1     # tidsintrvall i sekunder
tid_start = 0
tid_slutt = 15
N = int((tid_slutt - tid_start)/dt) # antall intervaller 

Pder = zeros(N+1)
P = zeros(N+1)
t = zeros(N+1)

t[0] = tid_start
P[0] = p0


for i in range(N):
    Pder[i] = k*P[i]*(1-(P[i]/B))
    P[i+1] = P[i] + Pder[i]*dt
    t[i+1] = t[i] + dt

plot (t,P, label="Populasjonsvekst")
xlabel("tid(måneder)")
ylabel("antall aper")
show()