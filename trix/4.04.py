personer = {}

while True:

    svar = input("Vil du fortsette? (y/n)\n> ")

    if svar == "y":
        navn = input("Oppgi et navn: ")

        # Denne blokken forsiker seg at alder er et heltall
        while True:
            try:
                alder = int(input("Oppgi en alder: "))
                break
            except ValueError:
                print("Oppgi gyldig alder")
                continue

        # legger inn navn og alder i ordbok
        personer[navn] = alder
    else:
        break

while True:

    bokstav = input("Oppgi en forbokstav: ")

    # sjekker at bruker taster inn en bokstav
    if bokstav.isalpha() and len(bokstav) == 1:
        break
    else:
        print("Oppgi gyldig input")


for key in personer:
    # sjekker at
    if key[:1].lower() == bokstav.lower():
        print (f"{key} er {personer[key]} år gammel")
else:
    print (f"Ingen personer med {bokstav} som forbokstav.")
