from pylab import *

# variabler og konstanter
B0 = 100  # cfu bakterier
R0 = 20

a = 0.15
b = 0.003
c = 0.001
d = 0.05
BE = 100


# tidsparameter 
dt = 0.05
t_start = 0
t_slutt = 140
N = int((t_slutt-t_start)/dt)

#Arrayer
t = zeros(N+1)
B = zeros(N+1)
R = zeros(N+1)

# initialisering
t[0] = t_start
B[0] = B0
R[0] = R0

# eulers metode
for i in range(N):
    Bder = a * B[i] - b * B[i] * R[i] # a * B[i] * (1-B[i]/BE) - b * B[i] * R[i]
    Rder = c * R[i] * B[i] - d * R[i]
    B[i+1] = B[i] + Bder*dt
    R[i+1] = R[i] + Rder*dt
    t[i+1] = t[i] + dt   

rc('axes', linewidth=5)
figure(figsize=(50,20))
plot(t,B,label='byttedyr',linewidth=10)
plot(t,R,label='rovdyr',linewidth=10)
xlabel('tid (timer)',size=50)
xticks(fontsize=50)
ylabel('population',size=50)
yticks(fontsize=50)
legend(prop={'size': 50})
show()