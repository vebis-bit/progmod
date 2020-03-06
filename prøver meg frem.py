from pylab import randint

teller = 0
for i in range(10):
    L2 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    L7 = []
    L8 = []
    L9 = []
    L10 = []
    L11 = []
    L12 = []
    N = 100000
    n = N/100
    
    teller+=1
    for i in range(N):
        terningkast = randint(1,7) + randint(1,7)
        if terningkast == 2:
            L2.append(terningkast)
        elif terningkast == 3:
            L3.append(terningkast)
        elif terningkast == 4:
            L4.append(terningkast)
        elif terningkast == 5:
            L5.append(terningkast)
        elif terningkast == 6:
            L6.append(terningkast)
        elif terningkast == 7:
            L7.append(terningkast)
        elif terningkast == 8:
            L8.append(terningkast)
        elif terningkast == 9:
            L9.append(terningkast)
        elif terningkast == 10:
            L10.append(terningkast)
        elif terningkast == 11:
            L11.append(terningkast)
        elif terningkast == 12:
            L12.append(terningkast)
    print(teller)
    print("sjansen for å få 2  er", len(L2)/n,"%")
    print("sjansen for å få 3  er",len(L3)/n,"%")
    print("sjansen for å få 4  er",len(L4)/n,"%")
    print("sjansen for å få 5  er",len(L5)/n,"%")
    print("sjansen for å få 6  er",len(L6)/n,"%")
    print("sjansen for å få 7  er",len(L7)/n,"%")
    print("sjansen for å få 8  er",len(L8)/n,"%")
    print("sjansen for å få 9  er",len(L9)/n,"%")
    print("sjansen for å få 10 er",len(L10)/n,"%")
    print("sjansen for å få 11 er",len(L11)/n,"%")
    print("sjansen for å få 12 er",len(L12)/n,"%")
    print("")


    