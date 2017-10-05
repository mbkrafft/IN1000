""" Koden viser hvordan man kan sende argumenter til funksjoner og returnere
verdier. """

# Legger sammen og returnerer to tall


def adder(tall1, tall2):
    return tall1 + tall2


# Bruker adder-funksjonen
resultat1 = adder(12, 42)
resultat2 = adder(134, 59)

print (f"Forste resultat er {resultat1} og andre resultat er {resultat2}")


# finner antall forekomster av bokstaven i teksten.
def tellForekomst(minTekst, minBokstav):
    return minTekst.count(minBokstav)


# ber bruker om bokstav og tekst
streng = input("Skriv inn en tekstreng: ")
bokstav = input("Skriv inn en bokstav: ")

# skriver ut forekomster av bokstaven i teksten ved å kalle på tellForekomst-funksjonen
print (tellForekomst(streng, bokstav))
