from pylab import *
x = linspace(-3,3,100)
y1 = x**15
y2 = x + 2
y3 = cos(x)

plot(x, y1,color='magenta',linestyle=':',
     marker=' ',label='x$^2$')
plot(x, y2, color='gold',linestyle='--',
     marker=' ',label='x + 2')
plot(x, y3, color='brown',linestyle='-',
     marker=' ',label='cos(x)')
legend()
plot()
grid()
ylim(-2,2)
title('Plott av x$^2$')
xlabel('x')
ylabel('y')
axhline(y=0,color='fuchsia')
axvline(x=0,color='seagreen')

show()