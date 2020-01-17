from pylab import *
from random import randint
import pygame
import os

ditt_valg = input("Hvilke tomter er best i Monopol?(Du skriver kun fargen) ")       #lager en inputvariabel for hvilke tomt man tror er best

pygame.init()                                           #starter pygame
pygame.mixer.init()                                     #starter pygame.mixer
clock = pygame.time.Clock()                             #lager klokke
vindu = pygame.display.set_mode((910, 540))             #lager et vindu i pygame
pygame.display.set_caption("Simulering av monopol?")    #overskrift
bg = pygame.image.load('bg.png')                        #bakgrunn
font = pygame.font.SysFont('comicsans', 60, True)
font1 = pygame.font.SysFont('arial', 60, True, True)    #fonter
font2 = pygame.font.SysFont('arial', 30)
frame_rate = 20                                         #globale variabler
antall_spill = 10000                                    #antall spill


class loading(object):                                  #gjør loading firkanten til et objekt
    def __init__(self, x, y, bredde, hoyde):            #spesifikasjoner og variabler til loadingfirkanten
        self.x_prikk = x
        self.y_prikk = y
        self.bredde_prikk = bredde
        self.hoyde_prikk = hoyde
        self.start_loading = bredde                     #startbredde
        self.visible = True                             #bestemmer om loading r synlig eller ikke
        self.x_text = self.x_prikk - 190                #hvor på skjermen teksten er
        self.y_text = self.y_prikk

    def draw(self, vindu):                              #tegne funksjonen til loadingobjektet
        if k < frame_rate * 10:                                     #utfører bare drawfunksjonen hvis k er mindre enn framerate akkuratt som i hovedloopen
            text = font.render('Loading: DONE', 1, (100, 55, 50))   #bruker font på text
            vindu.blit(text, (self.x_text, self.y_text))            #sender text til skjerm
            if self.visible:                                        #tegner firkantene for loading hvis visible er true
                pygame.draw.rect(vindu, (255,0,0), (self.x_prikk, self.y_prikk, self.bredde_prikk,self.hoyde_prikk))                                                    #firkant bak
                pygame.draw.rect(vindu, (0, 255, 255), (self.x_prikk, self.y_prikk, self.bredde_prikk - ((100 / 100) * (200 - self.start_loading)), self.hoyde_prikk))  #firkant som blir mindre
                if self.start_loading >= 0:                                                                                 #løkken som gjør den blp firkangen mindre
                        self.start_loading -= 1
                else:                                                                                                   #når den blå firkanten har 0 i bredde slutter løkka å kjøre
                    self.visible = False
    def tomter(self,vindu):                                                                                             #blitter litt av dataen til pygamevinduet, men bare etter at den forgje loopen er ferdig
        if k == frame_rate * 10:
            overskrift = font1.render('Resultater!', 1, (255,255,255))
            BRUN = font2.render('Gjennomsnitt brun     =  ' + str(brunF / antall_spill), 1, (0, 255, 255))
            LYS = font2.render('Gjennomsnitt lyseblå  =  ' + str(lyseblaaF / antall_spill), 1, (0, 255, 255))
            ROSA = font2.render('Gjennomsnitt rosa     =  ' + str(rosaF / antall_spill), 1, (0, 255, 255))
            ORA = font2.render('Gjennomsnitt oransje  =  ' + str(oransjF / antall_spill), 1, (0, 255, 255))
            ROD = font2.render('Gjennomsnitt rod      =  ' + str(rodF / antall_spill), 1, (0, 255, 255))
            GUL = font2.render('Gjennomsnitt gul      =  ' + str(gulF / antall_spill), 1, (0, 255, 255))
            GRO = font2.render('Gjennomsnitt grønn    =  ' + str(gronnF / antall_spill), 1, (0, 255, 255))
            BL = font2.render('Gjennomsnitt blå      =  ' + str(blaaF / antall_spill), 1, (0, 255, 255))
            win = font1.render('Det er helt riktig!!', 1, (255,255,255))
            nop = font1.render('Sjekk dataen oransje er best ;)', 1, (255,255,255))
            vindu.blit(overskrift, (60, 50))
            vindu.blit(BRUN, (100, 100))
            vindu.blit(LYS, (100, 120))
            vindu.blit(ROSA, (100, 140))
            vindu.blit(ORA, (100, 160))
            vindu.blit(ROD, (100, 180))
            vindu.blit(GUL, (100, 200))
            vindu.blit(GRO, (100, 220))
            vindu.blit(BL, (100, 240))
            if ditt_valg == "oransje" or ditt_valg == "Oransje" or ditt_valg == "oransj" or ditt_valg == "Oransj":      #bruker den globale variabelen til å bestemme om du gjettet riktig med rom for skrivefeil
                vindu.blit(win, (390, 270))
            else:
                vindu. blit(nop, (120, 270))

def redrawgamewindow():                                 #all tegningen som skjer på skjermen er samlet i en draw funksjon
    vindu.blit(bg, (0,0))                               #bakgrunn
    loading_bar.draw(vindu)                             #tenger loadingbar
    if monopol_simulering:
        overskrift = font1.render('MONOPOLSIMULERING UTFØRES', 1, (255, 255, 255))      #overskrift
        vindu.blit(overskrift, (60, 50))
    loading_bar.tomter(vindu)                           #data til skjerm
    pygame.display.update()                             #opdaterer skjerm

monopol_simulering = True
s = 0                                                   #globale variabler
k = 0
loading_bar = loading(390, 270, 200, 40)                #definerer verdiene til loading_bar
pygame.mixer.music.load(os.path.join("sanger", "Kahoot_Full_Original_Soundtrack.ogg"))          #loader musikk
pygame.mixer.music.play(-1)                             #starter musikken
#Hovedloopen
while True:
    clock.tick(frame_rate)                              #setter frame rate
    for ting in pygame.event.get():                     #lager et event
        while k < frame_rate*10:                        #kjører loadingscreen i 10 sekunder
            redrawgamewindow()
            k+=1
        else:                                                                                                           #når de 10 sekundene er over kjører monopolsimuleringen
            while monopol_simulering == True:
                brikke = 0
                fengsel = 0                             #definerer variablene for fengsel brikke og runde
                runder = 0
                teller = 0

                B = []
                LB = []
                Ro = []
                O = []                                  #lager en liste for hver av tomtgruppene
                R = []
                Gu = []
                Gr = []
                Bl = []

                brunF = 0
                lyseblaaF = 0
                rosaF = 0
                oransjF = 0                             #lager en hovedvariabel for hver av tomtgruppene som ikke skal nullstilles
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
                oransj1F = 0                            #lager en hovedvariabel for hver av de enkelte tomtene i spillet som ikke skal nullstilles
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

                for i in range(0, antall_spill):            #alle spillene
                    tall = randint(100, 200)                #antall kast et spill består av ligger ett sted mellom 100 og 200
                    brikke = 0                              #en variabel for brikken som skall nullstilles hver runde

                    brun1 = 0
                    brun2 = 0
                    lyseblaa1 = 0
                    lyseblaa2 = 0
                    lyseblaa3 = 0
                    rosa1 = 0
                    rosa2 = 0
                    rosa3 = 0                               # lager en variabel for hver enkel tomt som skal nullstilles for hvert spill
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
                    oransj = 0                              #lager en variabel for hver gruppe som skal nullstilles for hvert spill
                    rod = 0
                    gul = 0
                    gronn = 0
                    blaa = 0

                    for h in range(0, tall):                        #selve spillopen
                        brikke += randint(1, 6) + randint(1, 6)     #kaster to terninger og legger dem sammen
                        # start
                        if brikke == 40:                            #nullstiller briken når den når 40 eller over
                            teller += 1
                        if brikke > 40:
                            brikke -= 40
                            runder += 1
                        # fengsel
                        if brikke == 30:                            #gå direkte i fengsel hvis man lander på denne
                            brikke = 10
                            fengsel += 1                            #teller fengsel
                        # brun
                        if brikke == 1:                             #tellere for brun
                            brun1 += 1
                        if brikke == 3:
                            brun2 += 1

                        # lyseblå
                        if brikke == 6:                             #tellere for lyseblå
                            lyseblaa1 += 1
                        if brikke == 8:
                            lyseblaa2 += 1
                        if brikke == 9:
                            lyseblaa3 += 1

                        # rosa
                        if brikke == 11:                            #tellere for rosa
                            rosa1 += 1
                        if brikke == 13:
                            rosa2 += 1
                        if brikke == 14:
                            rosa3 += 1

                        # oransje
                        if brikke == 16:                            #tellere for oransje
                            oransj1 += 1
                        if brikke == 18:
                            oransj2 += 1
                        if brikke == 19:
                            oransj3 += 1

                        # rød
                        if brikke == 21:                            #tellere for oransje
                            rod1 += 1
                        if brikke == 23:
                            rod2 += 1
                        if brikke == 24:
                            rod3 += 1

                        # gul
                        if brikke == 26:                            #tellere for gul
                            gul1 += 1
                        if brikke == 27:
                            gul2 += 1
                        if brikke == 29:
                            gul3 += 1

                        # grønn
                        if brikke == 31:                            #tellere for grønn
                            gronn1 += 1
                        if brikke == 32:
                            gronn2 += 1
                        if brikke == 34:
                            gronn3 += 1
                        # blå
                        if brikke == 37:                            #tellere for blå
                            blaa1 += 1
                        if brikke == 39:
                            blaa2 += 1

                        brun = brun1 + brun2                                #legger sammen så man får sammenlagt av alle for hver enkelt farge
                        lyseblaa = lyseblaa1 + lyseblaa2 + lyseblaa3
                        rosa = rosa1 + rosa2 + rosa3
                        oransj = oransj1 + oransj2 + oransj3
                        rod = rod1 + rod2 + rod3
                        gul = gul1 + gul2 + gul3
                        gronn = gronn1 + gronn2 + gronn3
                        blaa = blaa1 + blaa2
                    B.append(blaa)
                    LB.append(lyseblaa)
                    Ro.append(rosa)                                         #legger til alle verdiene for tomtene i en liste så man kan fp ut data
                    O.append(oransj)
                    R.append(rod)
                    Gu.append(gul)
                    Gr.append(gronn)
                    Bl.append(blaa)

                    brun1F += brun1
                    brun2F += brun2

                    lyseblaa1F += lyseblaa1                                 #legger til verdien for tomtene i den variabelen som ikke skal nullstilles
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

                    brunF += brun
                    lyseblaaF += lyseblaa
                    rosaF += rosa
                    oransjF += oransj
                    rodF += rod
                    gulF += gul
                    gronnF += gronn
                    blaaF += blaa

                print("\n")
                print('Antall spill simulert: ', antall_spill)                                      #skriver ut antall spill
                print('antall runder simulert: ', runder)
                print("\n")
                print('Gjennomsnitt brun    = ', brunF / antall_spill)                              #skriver ut gjennomsnittlig antall ganger landet på en tomt
                print('Gjennomsnitt lyseblå = ', lyseblaaF / antall_spill)
                print('Gjennomsnitt rosa    = ', rosaF / antall_spill)
                print('Gjennomsnitt oransje = ', oransjF / antall_spill)
                print('Gjennomsnitt rod     = ', rodF / antall_spill)
                print('Gjennomsnitt gul     = ', gulF / antall_spill)
                print('Gjennomsnitt grønn   = ', gronnF / antall_spill)
                print('Gjennomsnitt blå     = ', blaaF / antall_spill)
                print("\n")
                print("Gjennomsnittlig ganger landet på start  = ", teller / antall_spill)
                print('Gjennomsnittlig antall ganger i fengsel = ', fengsel / antall_spill)
                print('Gjennomsnittlig antall runder per spill  = ', runder / antall_spill)
                print("\n")
                print("Parkveien = ", brun1F / antall_spill)
                print("Kirkeveien = ", brun2F / antall_spill)
                print("\n")
                print("Kongensgate = ", lyseblaa1F / antall_spill)
                print("Prinsensgate = ", lyseblaa2F / antall_spill)
                print("Øvre slottsgate = ", lyseblaa3F / antall_spill)
                print("\n")
                print("Nedre slotsgate = ", rosa1F / antall_spill)
                print("Trondheimsveien = ", rosa2F / antall_spill)
                print("Nobels gate = ", rosa3F / antall_spill)
                print("\n")
                print("Grensen = ", oransj1F / antall_spill)
                print("Gabels gate = ", oransj2F / antall_spill)
                print("Ringgaten = ", oransj3F / antall_spill)
                print("\n")
                print("Bygdøy Allé = ", rod1F / antall_spill)
                print("Skarpsno = ", rod2F / antall_spill)
                print("Slemdal = ", rod3F / antall_spill)
                print("\n")
                print("Karl Johanns gate = ", gul1F / antall_spill)
                print("Stortorget = ", gul2F / antall_spill)
                print("Torggata = ", gul3F / antall_spill)
                print("\n")
                print("Trosterudveien = ", gronn1F / antall_spill)
                print("Pilerstredet = ", gronn2F / antall_spill)
                print("Sinsen = ", gronn3F / antall_spill)
                print("\n")
                print("Ullevåll hageby = ", blaa1F / antall_spill)
                print("Rådhusplassen = ", blaa2F / antall_spill)
                print("\n")
                print("Frekvenshistogram over hvor mange runder en fatge har blitt landet på i løpet av et spill:")
                liste = linspace(0, int(tall / 4), int(tall / 4) + 1)                                                   #lager en liste for å normalisere histogramene
                hist(B, bins=liste, color='brown', edgecolor='black', density='true')                                   #lager og viser histogrammr over hvor mange runder en farge ble landet på i løpet av ett spill
                show()
                hist(LB, bins=liste, color='cyan', edgecolor='black', density='true')
                show()
                hist(Ro, bins=liste, color='pink', edgecolor='black', density='true')
                show()
                hist(O, bins=liste, color='orange', edgecolor='black', density='true')
                show()
                hist(R, bins=liste, color='red', edgecolor='black', density='true')
                show()
                hist(Gu, bins=liste, color='yellow', edgecolor='black', density='true')
                show()
                hist(Gr, bins=liste, color='green', edgecolor='black', density='true')
                show()
                hist(Bl, bins=liste, color='blue', edgecolor='black', density='true')
                show()
                monopol_simulering = False                                                                              #gjør monopolsimulering til false så løkken bare utføres en gang
                redrawgamewindow()                                                                                      #tegner pygame vinduet på nytt så man skal få opp dataen på skjermen og loadingscreen skal forsvinne
        if ting.type == pygame.QUIT:                                                                                    #krysse ut løkken hvis man
            pygame.QUIT()
            quit()