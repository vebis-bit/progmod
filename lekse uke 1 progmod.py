from pylab import *

n = 1000
R = list(linspace(2, n, n-1))
r = 0
while p**2 < n:
    p = R[r]
    for i in R:
        if i%p == 0 and i >= p**2:
            R.remove(i)
    r+=1
print(R)

















"""R = list(linspace(2, 100, 99))
PR = []
print(R)
p = 2
s = 0
for i in range(2, 100):
    p = R[s]
    s +=1
    if i%2 != 0:
        if i%3 !=0:
            if i%5 != 0:
                if i%7 != 0:
                    PR.append(i)

print(PR)"""