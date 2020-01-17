from pylab import *

data = loadtxt('fartgreie.txt',skiprows=1,delimiter=',')

tids = data[:,0]
høyde = data[:,2]



plot(tids, høyde)
grid()
xlabel('tid')
ylabel('høyde')
