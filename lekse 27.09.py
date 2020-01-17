#lekse - oppgave 4.7 og 4.9

#4.7
a = 0
n = 100


for i in range(0, n):
    a+= 3/3**i
print(a)

#4.9
mål = float(input("sett deg et mål "))   #sluttsum i kr
startsum = float(input("startsumm "))   #start sum i kr
rente = float(input("rentesumm "))   #rente i prosent
tid = 0         #tid i måneder
summen = startsum

while startsum <= mål:
    startsum += startsum*(rente/100)
    tid += 1
print("hvis du setter inn ", summen, " tar det ", tid, "år hvis du har en rente på", rente, "%")

