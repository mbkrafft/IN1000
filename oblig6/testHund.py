""" Tester hundeklassen fra hund.py """

from hund import Hund


def hovedprogram():

    hund1 = Hund(10, 30)

    print(f"Hundens alder er: {hund1.hentAlder()}")

    print(f"Hundens vekt er: {hund1.hentVekt()}")

    print ("")

    # Kjorer helt til vi ser at funksjonaliteten om a gaa ned i vekt funker
    for i in range(6):
        print (f"Spring nummer {i+1}")
        hund1.spring()
        print(f"Hundens vekt er naa: {hund1.hentVekt()}")

    print("")

    # Kjorer helt til vi ser at funksjonaliteten om a gaa opp i vekt funker
    for i in range(6):
        print (f"Spis nummer {i+1}")
        hund1.spis(1)
        print(f"Hundens vekt er naa: {hund1.hentVekt()}")


hovedprogram()
