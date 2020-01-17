from math import sqrt
def kvadratrot(a, x0, N):
    """
    a: det vi skal ha kvadratroten av
    x0: satrtgjett
    N: antall iterasjoner
    """
    x = x0    
    for i in range(N):
        x = 0.5*(x + a/x)
    return x

rot = kvadratrot(12,100,10)

print("numerisk", rot, "antalytisk", sqrt(12))