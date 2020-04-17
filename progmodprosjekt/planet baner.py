from pylab import *
a = 0
b = 1.88
N = 10000
t = linspace(a,b,N)
dt = t[1]-t[0]

P = 0
with open("planeter_data.dat","r") as  infile:
    P =int(infile.readline ())
    pos = zeros([N,2,P])
    fart = zeros([N,2,P])
    masse = zeros(N)
    for i,line in enumerate(infile):
        data = line.split()
        x =float(data [1])
        y =float(data [2])
        fx =float(data [3])
        fy =float(data [4])
        m =float(data [5])
        
        pos[0,:,i] = array([x,y])
        fart[0,:,i] = array([fx ,fy])
        masse[i] = m

G = 4*pi**2
m_sol = 1
for i in range(N-1):
    for j in range(P):
        pos_planet = pos[i,:,j]
        fart_planet = fart[i,:,j]
        
        # Fra  sola
        r = norm(pos_planet)
        a = -G*m_sol*pos_planet/r**3
        for k in range(P):
            if k != j:# hente  ut  bidrag  fra  andre  planeter
                pos_andreplanet = pos[i,:,k]
                fart_andreplanet = fart[i,:,k]
                rr = norm(pos_planet -pos_andreplanet)
                a  -= G*masse[k]*(pos_planet  -pos_andreplanet)/rr**3
        fart[i+1,:,j] = fart[i,:,j] + dt*a
        pos[i+1,:,j] = pos[i,:,j] + dt*fart[i+1,:,j]

for p in range(P):
    x = pos[:,0,p]
    y = pos[:,1,p]
    plot(x,y)

plot(0,0,"yo")

show()