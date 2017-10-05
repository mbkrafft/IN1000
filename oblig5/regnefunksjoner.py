""" Koden under viser hvordan ulike regnefunksjoner kan gjores i python """

# en funksjon som legger sammen to verdier


def addisjon(a, b):
    return a + b

# en funksjon som trekker en verdi b fra en verdi a


def subtraksjon(a, b):
    return a - b

# en funksjon som deler verdi a på verdi b


def divisjon(a, b):
    return float(a) / float(b)

# en funksjon son konverterer en verdi til en annen verdi


def tommerTilCm(antallTommer):
    assert float(antallTommer) > 0, "Gi antall tommer storre enn 1"

    return float(antallTommer) * 2.54

# en funksjon som skriver ut beregningene i funksjonene over


def skrivBeregninger():

    print ("\nUtregninger:")
    while True:
        try:
            a = float(input("skriv inn tall1: "))
            b = float(input("skriv inn tall2: "))
        except ValueError:
            print ("skriv inn tall")
            continue

        break

    print (f"Resultat av addisjon: {addisjon(a, b)}")
    print (f"Resultat av substraksjon: {subtraksjon(a, b)}")
    print (f"Resultat av divisjon: {divisjon(a, b)}")

    print ("\nKonvertering fra tommer til cm:")
    while True:
        try:
            c = float(input("skriv inn tommer som du vil gjore til cm: "))
        except ValueError:
            print ("skriv inn tall")
            continue

        break

    print (f"Resultat av konvertering: {tommerTilCm(c)}")

# en funksjon som tester om funksjonene overfor fungerer som de skal


def testFunksjoner():
    assert subtraksjon(5, 3) == 2, "feil"
    assert subtraksjon(-5, -3) == -2, "feil"
    assert subtraksjon(5, -5) == 10, "feil"

    assert divisjon(5, 5) == 1, "feil"
    assert divisjon(0, 1) == 0, "feil"
    assert divisjon(-5, 2) == -2.5, "feil"

    assert tommerTilCm(1) == 2.54, "feil"
    # sjekker om assert faktisk funker med kommentert ut kode
    # print (tommerTilCm(-1))


# legger til denne for at koden ikke skal kjøres dersom modulen blir importert
if __name__ == "__main__":
    skrivBeregninger()
    testFunksjoner()
