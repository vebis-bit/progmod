import matplotlib.pyplot as plt
import numpy as np

bilde = plt.imread("valler.png")
plt.imshow(bilde)
plt.savefig("original.png") # Lagrer originalen som backup/referanse
dx = 1

dfdx = (bilde[1:-1,2:,:] - bilde[1:-1,1:-1,:])/dx # Deriverer i x-retning
plt.imshow(2*abs(dfdx))
plt.savefig("dfdx.png", dpi = 1000)

dfdy = (bilde[2:,1:-1,:] - bilde[1:-1,1:-1,:])/dx # Deriverer i y-retning
plt.imshow(2*abs(dfdy))
plt.savefig("dfdy.png", dpi = 1000)

grad = np.sqrt(dfdx**2 + dfdy**2) # Kombinerer den deriverte i x- og y-retning (gradienten)
plt.imshow(4*grad)                 # Ganger med 3 for å gjøre fargeforskjellene tydeligere
plt.savefig("grad.png", dpi = 1000)
