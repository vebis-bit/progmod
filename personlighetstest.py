#personlighetstest
print("hei og velkommen til dette personlighetsspillet, i dette spillet er det noen regler. for å svare ja skriver man tallet (1), for å si nei skriver man tallet (2). \ vil du starte spill?")
ja = "1"
nei = "2"
gameover = "GAME OVER, MF!!!"
startspill = input("start spillet: ")
if startspill == ja:
    valg1 = input("lilker du pølse?")
    if valg1 == ja:
        print("ok.")
        valg2 = input("bruker du ketchupå på pølse?")
        if valg2 == ja:
            print("ok, neste spørsmål")
            valg31 = input("er Chilliketchup innafor?")
            if valg31 == ja:
                print("wow, du er en skikkelig type du, la oss ta dette til det neste levelet.")
                valg41 = input("spiser du pølse i: \1. hånda? \2. med kniv og gaffel?")
                if valg41 == ja:
                    print("Du er en som liker å leve livet i det fri, og ha det gøy, bare et spørsmål igjen.")
                    valg51 = input("du er helt klart en person med stil, men har du like mye klasse som mr. peanut?")
                    if valg51 == ja:
                        print("Du har enten sett the office, og er den perfekte person, eller bare tror du har klasse...")
                        valg61 = input("ok, det var selvfølgelig et ledende spørsmål, har du sett the office?")
                        if valg61 == ja:
                            print("ja du er faktisk den perfekte person, og derfor vil jeg bare gi deg en klapp på skulderen og en mulighet til å ringen meg;) 92204940 ")
                        elif valg61 == nei:
                            print("du var nære, og jeg vil si du hadde en ganske god sjanse, men du vil aldri nå helt opp:")
                    elif valg51 == nei:
                        print("du er sikkert gansk forvirret nå, hvem er mr peanut?, vel du fortjener ikke å vi vite det din taper", gameover)
                elif valg41 == nei:
                    print("ahhhh jeg begynner å skjønne at du er en person med klasse, keep it up!")
                    valg52 = input("liker du best \1. wienerpølse eller \2. grillpølse?")
                    if valg52 == ja:
                        print("nei, nei, nei, du kan ikke spise wienerpølse med kniv og gaffel...")
                    elif valg52 == nei:
                        print("det er innfaor så lenge du har potetstappe.")
                        valg62 = input("dette var selvfølegelig et ledende spørsmål, spiser du pølse med potetstappe?")
                        if valg62 == ja:
                            print("dette er et meget godt tegn, ingenting galt i å spise pølse med kniv og gaffel, så lenge det er med potetmos.")
                        elif valg62 == nei:
                            print("Du er syk, du trenger hjelp, vær så snill og ikke rør en pc noen sinne i ditt liv")
            elif valg31 == nei:
                print("ok, du lever på kanten, men her kommer det avgjørende spørsmålet")
                valg42 = input("har du senep på pølsa med ketchup?")
                if valg42 == ja:
                    print("du har fått nok sjanser, du er en ekkel person, med dårlige vaner. få litt klasse")
                    print(gameover)
                elif valg42 == nei:
                    print("jeg viste du hadde det i deg, dette var helt klart et steg i den riktige retningen")
                    valg53 = input("spiser du pølse i: \1. hånda? \2. med kniv og gaffel?")
                    if valg53 == ja:
                        print("Du er en som liker å leve livet i det fri, og ha det gøy, bare et spørsmål igjen.")
                        valg63 = input("du er helt klart en person med stil, men har du like mye klasse som mr. peanut?")
                        if valg63 == ja:
                            print("Du har enten sett the office, og er den perfekte person, eller bare tror du har klasse...")
                            valg71 = input("ok, det var selvfølgelig et ledende spørsmål, har du sett the office?")
                            if valg71 == ja:
                                print("ja du er faktisk den perfekte person, og derfor vil jeg bare gi deg en klapp på skulderen og en mulighet til å ringen meg;) 92204940 ")
                            elif valg71 == nei:
                                print("du var nære, og jeg vil si du hadde en ganske god sjanse, men du vil aldri nå helt opp:")
                        elif valg63 == nei:
                            print("du er sikkert gansk forvirret nå, hvem er mr peanut?, vel du fortjener ikke å vi vite det din taper", gameover)
                    elif valg53 == nei:
                        print("ahhhh jeg begynner å skjønne at du er en person med klasse, keep it up!")
                        valg64 = input("liker du best \1. wienerpølse eller \2. grillpølse?")
                        if valg64 == ja:
                            print("nei, nei, nei, du kan ikke spise wienerpølse med kniv og gaffel...")
                        elif valg64 == nei:
                            print("det er innfaor så lenge du har potetstappe.")
                            valg72 = input("dette var selvfølegelig et ledende spørsmål, spiser du pølse med potetstappe?")
                            if valg72 == ja:
                                print("dette er et meget godt tegn, ingenting galt i å spise pølse med kniv og gaffel, så lenge det er med potetmos.")
                            elif valg72 == nei:
                                print("Du er syk, du trenger hjelp, vær så snill og ikke rør en pc noen sinne i ditt liv")
        elif valg2 == nei:
            print("ok, jeg ser med en gang at du er en stilig fyr og vil derfor gå en anne retnig med dette.")
            valg32 = input("spiser du pølse i: \1. hånda? \2. med kniv og gaffel?")
            if valg32 == ja:
                print("og her gir jeg deg ros også skuffer du meg på denne måten, jeg vil gi deg game over, men skal gi deg en sjanse til.")
                valg43 = input("spiser du i \1. lompe? \2. brød?")
                if valg43 == ja:
                    print("wow nå imponerer du, men er du klar for dette smpørsmålet?")
                    valg54 = input("har du prøvd pølse i vaffel?")
                    if valg54 == ja:
                        print("jeg også, ikke ille ikkesant?")
                        valg65 = input("på pølse i vaffel, hva har man på da? \1. ketcup \2. syltetøy \3. begge ")
                        if valg65 == ja:
                            print("wow git jo mening, men fortsatt høres rart ut ikkesant?")
                            valg73 = input()
                        elif valg65 == nei:
                            print("ok, dette er for rart, selvom det gir litt mening, men bare nei plis...")
                            input()
                        else:
                            print("ok nå trår du over grensen her, og det er nettopp det jeg har lett etter, derfor har jeg tekt til å ta deg med til det hemmelige nye nivået.")
                            ekstravalg1 = input("vil du lage en historie?")
                            if ekstravalg1 == ja:
                                print("ok, la oss sette i gang, reglene er jeg skriver historien og du forteller meg hvilke retning jeg skal gå i.")
                                ekstravalg2 = input()
                            elif ekstravalg1 == nei:
                                print("ok, tilbake til spørsmål da.")
                elif valg43 == nei:
                    print("brød er godt til tider det også, men for meg vil jeg si at du svarte feil")
                    valg55 = input()
            elif valg32 == nei:
                print("dette er lovende, men er du klar for å ta dette til et nytt nivå?")
                valg44 = input("du er en person med klasse, men er du mr peanut classy?")
                if valg44 == ja:
                    print("du har enten sett the office, og er den perfekte person, eller bare tror du har klasse...")
                    valg56 = input()
                elif valg44 == nei:
                    print("du er sikkert gansk forvirret nå, hvem er mr peanut?, vel du fortjener ikke å vi vite det din taper", gameover)
    elif valg1 == nei:
        print("Ok, jeg har sett nok. du er ikke kvalifisert til å ta denne testen...", gameover)
else:
    print(gameover)