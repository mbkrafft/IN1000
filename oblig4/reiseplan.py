""" Koden viser hvordan nøstede lister fungerer """


steder = []
klesplagg = []
avreisedatoer = []
reiseplan = [steder, klesplagg, avreisedatoer]

for ganger in range(5):
    steder.append(input("Hvor vil du reise? \n> "))
    klesplagg.append(input("Hva vil du ha på deg? \n> "))
    avreisedatoer.append(input("Når vil du dra? \n> "))


for liste in reiseplan:
    print (f"{liste}\n")


while True:
    try:
        i1 = int(input("Skriv inn index for å hente liste: "))
        i2 = int(input("Skriv inn index for å finne frem i listen: "))
        break
    except ValueError:
        print ("Skriv inn ett tall motherfucker")
        continue


if (0 <= i1 < (len(reiseplan))) and (0 <= i2 < (len(reiseplan[i1]))):
    print (reiseplan[i1][i2])
else:
    print ("Ugyldig input!")
