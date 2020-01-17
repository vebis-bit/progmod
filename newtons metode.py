
def f(x):
    return x**5 - x**4 + x - 3

def fder(x, dx=1E-8):
    return (f(x+dx)-f(x))/dx

def newton(x,f,fder, tol=1E-8):
    teller = 0
    while abs(f(x)) > tol and teller < 100:
        x = x- f(x)/fder(x)
        teller += 1
    return x, teller



print(newton(10, f, fder))