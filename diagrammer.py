from pylab import *

fag = ['R2', 's2', 'kjemi 2', 'Fysikk 2', 'Tekforsk', 'Mattematikk', 'Biologi 2']


antall = loadtxt('testdata.txt',skiprows=1,delimiter=',')

hoyder = antall[:,1]

hist(hoyder)