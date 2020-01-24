from pylab import linspace


n = 100000
R = list(linspace(2, n, n-1))
r = 0
p = R[r]
while p**2 < n:
    p = R[r]
    for i in R:
        if i%p == 0 and i >= p**2:
            R.remove(i)
            
    r+=1
    print(r)
print(R, r,len(R))
