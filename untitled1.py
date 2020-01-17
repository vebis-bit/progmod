from pylab import *

data = loadtxt('solflekkertest.txt',skiprows=1,delimiter=',')

måneder = data[:,0]
solflekker = data[:,1]

plot(måneder, solflekker)
grid()
xlabel('år')
ylabel('antall solflekker')

snitt = mean(solflekker)
avvik = std(solflekker)

print('snitt', snitt, 'avvik', avvik)