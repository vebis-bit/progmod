from pylab import *
from random import randint


brikke = 0
fengsel = 0
runder = 0
teller = 0

B = []
LB = []
Ro = []
O = []
R = []
Gu = []
Gr = []
Bl = []

brunF = 0
lyseblaaF = 0
rosaF = 0
oransjF = 0
rodF = 0
gulF = 0
gronnF = 0
blaaF = 0

brun1F = 0
brun2F = 0
lyseblaa1F = 0
lyseblaa2F = 0
lyseblaa3F = 0
rosa1F = 0
rosa2F = 0
rosa3F = 0
oransj1F = 0
oransj2F = 0
oransj3F = 0
rod1F = 0
rod2F = 0
rod3F = 0
gul1F = 0
gul2F = 0
gul3F = 0
gronn1F = 0
gronn2F = 0
gronn3F = 0
blaa1F = 0
blaa2F = 0 



antall_spill = 10000
for i in range(0,antall_spill):
    tall = randint(50, 100)
    brikke = 0
    
    brun1 = 0
    brun2 = 0
    lyseblaa1 = 0
    lyseblaa2 = 0
    lyseblaa3 = 0
    rosa1 = 0
    rosa2 = 0
    rosa3 = 0
    oransj1 = 0
    oransj2 = 0
    oransj3 = 0
    rod1 = 0
    rod2 = 0
    rod3 = 0
    gul1 = 0
    gul2 = 0
    gul3 = 0
    gronn1 = 0
    gronn2 = 0
    gronn3 = 0
    blaa1 = 0
    blaa2 = 0 
     
    brun = 0
    lyseblaa = 0
    rosa = 0
    oransj = 0
    rod = 0
    gul = 0
    gronn = 0
    blaa = 0
    
    for h in range(0, tall):
        brikke += randint(1, 6)+randint(1,6)
        #start
        if brikke ==40:
            teller+=1
        if brikke > 40:
            brikke -= 40
            runder += 1
        #fengsel  
        if brikke == 30:
            brikke = 10
            fengsel += 1
        #brun   
        if brikke == 1:
            brun1 += 1
        if brikke == 3:
            brun2 += 1

        #lyseblå
        if brikke == 6:
            lyseblaa1 += 1
        if brikke == 8:
            lyseblaa2 += 1
        if brikke == 9:
            lyseblaa3 += 1

        #rosa
        if brikke == 11:
            rosa1 += 1
        if brikke == 13:
            rosa2 += 1
        if brikke == 14:
            rosa3 += 1

        #oransj
        if brikke == 16:
            oransj1 += 1
        if brikke == 18:
            oransj2 += 1
        if brikke == 19:
            oransj3 += 1
        
        #rød
        if brikke == 21:
            rod1 += 1
        if brikke == 23:
            rod2 += 1
        if brikke == 24:
            rod3 += 1

        #gul
        if brikke == 26:
            gul1 += 1
        if brikke == 27:
            gul2 += 1
        if brikke == 29:
            gul3 += 1
        #grønn
        if brikke == 31:
            gronn1 += 1
        if brikke == 32:
            gronn2 += 1
        if brikke == 34:
            gronn3 += 1
        #blå
        if brikke == 37:
            blaa1 += 1
        if brikke == 39:
            blaa2 += 1
            
    
        brun = brun1+brun2
        lyseblaa = lyseblaa1+lyseblaa2+lyseblaa3
        rosa = rosa1+rosa2+rosa3
        oransj = oransj1+oransj2+oransj3
        rod = rod1+rod2+rod3
        gul = gul1+gul2+gul3
        gronn = gronn1+gronn2+gronn3
        blaa = blaa1+blaa2      
    B.append(blaa)
    LB.append(lyseblaa)
    Ro.append(rosa)
    O.append(oransj)
    R.append(rod)
    Gu.append(gul)
    Gr.append(gronn)
    Bl.append(blaa)
    
    brun1F += brun1
    brun2F += brun2

    lyseblaa1F += lyseblaa1
    lyseblaa2F += lyseblaa2
    lyseblaa3F += lyseblaa3

    rosa1F += rosa1
    rosa2F += rosa2
    rosa3F += rosa3

    oransj1F += oransj1  
    oransj2F += oransj2
    oransj3F += oransj3

    rod1F += rod1
    rod2F += rod2
    rod3F += rod3

    gul1F += gul1
    gul2F += gul2
    gul3F += gul3

    gronn1F += gronn1
    gronn2F += gronn2
    gronn3F += gronn3

    blaa1F += blaa1
    blaa2F += blaa2
    
    brunF+=brun
    lyseblaaF+=lyseblaa
    rosaF+=rosa
    oransjF+=oransj
    rodF+=rod
    gulF+=gul
    gronnF+=gronn
    blaaF+=blaa

print("\n")
print('Antall spill simulert: ', antall_spill)
print('antall runder simulert: ', runder)
print("\n")
print('Gjennomsnitt brun    = ', brunF/antall_spill)
print('Gjennomsnitt lyseblå = ', lyseblaaF/antall_spill)
print('Gjennomsnitt rosa    = ', rosaF/antall_spill)
print('Gjennomsnitt oransje = ', oransjF/antall_spill)
print('Gjennomsnitt rod     = ', rodF/antall_spill)
print('Gjennomsnitt gul     = ', gulF/antall_spill)
print('Gjennomsnitt grønn   = ', gronnF/antall_spill)
print('Gjennomsnitt blå     = ', blaaF/antall_spill)
print("\n")
print("Gjennomsnittlig ganger landet på start  = ", teller/antall_spill)
print('Gjennomsnittlig antall ganger i fengsel = ', fengsel/antall_spill)
print('Gjennomsnittlig antall runder per spill  = ', runder/antall_spill)
print("\n")
print("Parkveien = ", brun1F/antall_spill)
print("Kirkeveien = ",brun2F/antall_spill)
print("\n")
print("Kongensgate = ", lyseblaa1F/antall_spill)
print("Prinsensgate = ", lyseblaa2F/antall_spill)
print("Øvre slottsgate = ", lyseblaa3F/antall_spill)
print("\n")
print("Nedre slotsgate = ",rosa1F/antall_spill)
print("Trondheimsveien = ", rosa2F/antall_spill)
print("Nobels gate = ", rosa3F/antall_spill)
print("\n")
print("Grensen = ", oransj1F/antall_spill)
print("Gabels gate = ", oransj2F/antall_spill)
print("Ringgaten = ", oransj3F/antall_spill)
print("\n")
print("Bygdøy Allé = ", rod1F/antall_spill)
print("Skarpsno = ", rod2F/antall_spill)
print("Slemdal = ", rod3F/antall_spill)
print("\n")
print("Karl Johanns gate = ", gul1F/antall_spill)
print("Stortorget = ", gul2F/antall_spill)
print("Torggata = ", gul3F/antall_spill)
print("\n")
print("Trosterudveien = ", gronn1F/antall_spill)
print("Pilerstredet = ", gronn2F/antall_spill)
print("Sinsen = ", gronn3F/antall_spill)
print("\n")
print("Ullevåll hageby = ", blaa1F/antall_spill)
print("Rådhusplassen = ", blaa2F/antall_spill)
print("\n")
print("Frekvenshistogram over hvor mange runder en viss farge har blitt landet på x antall ganger:")
liste=linspace(0,int(tall/4),int(tall/4)+1)
hist(B,bins=liste, color='brown', edgecolor='black',density='true')
show()
hist(LB,bins=liste, color='cyan', edgecolor='black',density='true')
show()
hist(Ro,bins=liste, color='pink', edgecolor='black',density='true')
show()
hist(O,bins=liste, color='orange', edgecolor='black',density='true')
show()
hist(R,bins=liste, color='red', edgecolor='black',density='true')
show()
hist(Gu,bins=liste, color='yellow', edgecolor='black',density='true')
show()
hist(Gr,bins=liste, color='green', edgecolor='black',density='true')
show()
hist(Bl,bins=liste, color='blue', edgecolor='black',density='true')
show()










