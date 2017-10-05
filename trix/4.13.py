# oppgave a
tall = []

while True:

    # bruker try/except for aa forsikre at vi faar gyldig input
    try:
        x = int(input("Skriv inn et heltall: "))
        tall.append(x)
    except ValueError:
        print ("Skriv inn gyldig input")
        continue
    # forutsett at try/execpt er greit, sjekker denne koden
    else:
        if len(tall) >= 5:
            break

print (tall)


# oppgave b
total = 0
for item in tall:
    total = total + item

print (total)


# oppgave c
for item in tall:
    if item > 10:
        print (item)


# oppgave d
for item in tall:
    if item == 5:
        print ("Tallet 5 finnes i listen")
