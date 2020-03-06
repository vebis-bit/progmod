from pylab import *
usikkerhet = 0.5
y1 = 37.8+usikkerhet/r-usikkerhet
y2 = 42.5+usikkerhet/r-usikkerhet
y3 = 60.4+usikkerhet/r-usikkerhet
r = 137.5
N1 = arctan(y1) * 180/math.pi
N2 = arctan(y2) * 180/math.pi
N3 = arctan(y3) * 180/pi
print('max theta 1: ', N1,'max theta 2: ', N2, 'max theta 3: ', N3)
