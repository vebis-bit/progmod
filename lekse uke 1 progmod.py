from pylab import linspace
from PIL import Image
import numpy as np

w,h = 250,250
n = w*h
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


data = np.zeros((h,w), dtype=np.uint8)

for k in R:
    x = int(k%w)
    y = int(k/h)
    data[y, x] = 255
    

img = Image.fromarray(data)
img.show()

