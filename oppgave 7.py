from math import *
def f(x):
    return x**5 - x**4 + x - 3

def fder(x, dx=1E-8):
    return (f(x+dx)-f(x))/dx

def newton(f,fder,t, v0,theta, tol=1E-8):
    teller = 0
    while abs(y(t,theta,v0)) > tol and teller < 100:
        t = t- y(t,theta,v0)/yder(t, theta, v0)
        teller += 1
    return t, teller

def y(t,theta,v0):
    g = 9.81
    return v0*sin(theta)*t - 0.5*g*t**2

def yder(t, theta, v0):
    g = 9.81
    return v0*sin(theta) - g*t

def x(t,v0):
    return v0*cos(theta)*t

tid = newton(y,yder,10, 18, pi/10)

print(tid)
