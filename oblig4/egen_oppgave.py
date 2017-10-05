"""Et   forslag   er   å programmere   et   system   som   lar   bruker   holde   styr   på,   legge   til   og   skrive   ut   venners bursdager."""

# Lag et system som lar bruker holde styr på, legge til og skrive ut venners
# bursdager. Skriv en while-lokke som går løpende. Spør om bruker vil se,
# legge til eller fjerne bursdager eller avslutte.


print ("Velkommen til bursdagskalenderen!")

# lager en tom ordbok
bursdager = {}

# while-løkke som går helt til brukeren taster inn avslutt
while True:

    print ("\n\n\n\n\n")
    svar = input("Hva vil du gjøre? (se/legge til/fjerne/avslutte)\n> ")

    if svar == "se":
        if len(bursdager) == 0:
            print ("Du har ikke lagt noe")
        for item in bursdager:
            print (f"{item} ble født: {bursdager[item]}")

    elif svar == "legge til":
        navn = input("Hvem sin bursdag vil du legge til? ")
        dato = input("Når er personen født? (YYYY-MM-DD)\n> ")
        bursdager[navn] = dato

    elif svar == "fjerne":
        while True:  # while-løkke som går til navn i ordboken tastes inn
            navn = input("Hvem sin bursdag vil du fjerne? ")
            if navn in bursdager:
                break
            if navn == "Angre":
                break
            print ("Skriv et navn som er i kalenderen!")
        if navn != "Angre":
            del bursdager[navn]

    elif svar == "avslutte":
        print ("Avslutter bursdagskalenderen.")
        break

    else:
        print ("Skriv et gyldig svar.")
