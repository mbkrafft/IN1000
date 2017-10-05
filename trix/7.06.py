beholdning = {}

while True:

    fortsette = input("Vil du fortsette? (y/n)\n> ")
    if fortsette.lower() == "y":
        while True:
            gronnsak = input("Skriv inn en gronnsak du vil legge til\n> ")
            try:
                pris = int(input("Skriv inn prisen til gronnsaken\n> "))
                break
            except ValueError:
                print ("Oppgi et gyldig input. (heltall). Prøv å legge til igjen")
                continue
            beholdning[gronnsak] = pris
            continue
    elif fortsette.lower() == "n":
        break
    else:
        print ("Skriv et gyldig input.")


for item in beholdning:
    print (f"{item} koster: {beholdning[item]} kr.")
