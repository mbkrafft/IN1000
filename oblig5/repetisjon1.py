""" Koden under er litt repetisjon paa tidligere konsepter """


mineOrd = []

# en funksjon som konkatenerer to tekststrenger


def slaaSammen(streng1, streng2):
    return streng1 + streng2

# en funksjon som skriver hvert element i en liste ut paa en ny linje


def skrivUt(liste):
    for item in liste:
        print(item)


# legger til denne for at koden ikke skal kjøres dersom modulen blir importert
if __name__ == "__main__":
    # løkke som kjører til en bruker sier ifra om aa avslutte
    while True:

        # faar input av bruker for å se hva bruker vil gjore
        svar = input("Vil du fortsette? (i for input / u for skrive ut / s for avslutte)\n> ")

        # sjekker hvilken condition som er sann og endrer funksjonalitet ut ifra
        # hva bruker har hatt bedt om
        if svar == "i":
            streng1 = input("Skriv inn tekststreng1: ")
            streng2 = input("Skriv inn tekststreng1: ")
            mineOrd.append(slaaSammen(streng1, streng2))

        elif svar == "u":
            skrivUt(mineOrd)

        elif svar == "s":
            break
        # hvis ingen av de gyldige svarene har blitt oppdaget, ber bruker om aa
        # skrive inn gyldig svar og fortsetter while-lokken
        else:
            print ("Skriv et gyldig svar")
