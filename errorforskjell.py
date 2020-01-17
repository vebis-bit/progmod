from pylab import * 
from sklearn.metrics import r2_score

T = array([0, 20, 40, 60, 80, 100])
sol_NH3 = array([88.5, 56.0, 34.0, 20.0, 11.0, 7.0])
sol_NaCl = array([35.7, 35.9, 36.4, 37.1, 38.0, 39.2])


#regresjon
grad = 3
reg_NH3 = polyfit(T, sol_NH3, grad)
#print(reg_NH3)

x = linspace(0,250, 10000)
a = reg_NH3[0]
b = reg_NH3[1]
c = reg_NH3[2]
d = reg_NH3[3]
y = a*x**3 + b*x**2 + c*x + d
y_R2 = a*T**3 + b*T**2 + c*T + d

R2 = r2_score(sol_NH3, y_R2)
print(R2)


scatter(T,sol_NH3, color = "blue")
plot(x, y, color = "red")
grid()
ylim(0)
show()