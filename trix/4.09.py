
skattekart = []
stoerrelse = 5

# Lag storrelse antall lister
for e in range(stoerrelse):
    a = []

    # Fyll listene med bokstaven "O"
    for e in range(stoerrelse):
        a.append("O")

    # Legg til hver "O"-liste i skattekart-listen vaar
    skattekart.append(a)


# Legger skatten paa en plass
while True:

    # tar inn brukerinput
    try:
        x = int(input("Skriv et x-koordinat til skatten: "))
        y = int(input("Skriv et y-koordinat til skatten: "))
    # dersom bruker skriver inn noe annet enn et heltall, prover igjen
    except ValueError:
        print ("Skriv et gyldig input")
        continue

    # sjekker om koordinatet ligger paa skattekartet
    if 0 <= x <= 4 and 0 <= y <= 4:
        skattekart[y][x] = "X"
        break
    else:
        print ("Skriv et gyldig input")


for i in range(20):
    print ("\n")


for i in range(3):

    while True:
        # tar inn brukerinput
        try:
            x = int(input("Skriv et x-koordinat hvor du tror skatten er: "))
            y = int(input("Skriv et y-koordinat hvor du tror skatten er: "))
        # dersom bruker skriver inn noe annet enn et heltall, prover igjen
        except ValueError:
            print ("Skriv et gyldig input")
            continue

        # sjekker om gyldig input, bryter ut av while-løkka om input er gyldig
        if 0 <= x <= 4 and 0 <= y <= 4:
            break
        else:
            print ("Skriv et gyldig input")
            continue

    # sjekker om spiller2 fant skatten eller ikke. Bryter ut av for-løkka
    # om spiller2 fant den.
    if skattekart[x][y] == "X":
        print ("Gratulerer du fant skatten!")
        break
    else:
        skattekart[x][y] = "#"
        print("Du fant desverre ikke skatten denne gangen.")

# skriver ut skattekart
for e in skattekart:
    for f in e:
        print (f, end="")  # Parameteret end="" soerger for at vi ikke faar linjeskift enda
    print("")
