"""lekse oppgave 4.1
programmet har en feil, timer er ikke definert.
hvis man ser bort i fra det, vil programmet hvor mye man tjener med en hvis timeslønn der man selv putter inn timer.
hvis man har jobbet mer enn man trenger, vil programmet også beregne hvor mye penger det blir med overtidsbetaling.
"""

timer = float(input("hvor mange timer har du jobbet: "))

timelonn = 150
arbeidsuke = 40
overtid = 0
#skoleting = 26*30*13

if timer <= 40:
    overtid = 0
    print(timelonn * timer + 1.5 * timelonn * overtid)
    #print(timelonn * timer * skoleting + 1.5 * timelonn * overtid)
else:
    overtid = timer - arbeidsuke
    print(timelonn * timer + 1.5 * timelonn * overtid)
#print(skoleting)