"""
Skriv oppgavetekst til en oppgave som handler om innlesing fra fil og funksjoner. Eller du kan følge dette forslaget: Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil der hver linje beskriver et navn på et mål og selve målet i tommer. Formatet vil se slik ut:

Skulderbredde 4
Halsvidde 3.2
Livvidde 10

La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål og benytter seg av  tommerTilCm  som du skrev tidligere for å skrive ut målene i centimeter.
"""

# Obs! Pass paa at baade egen_oppgave.py og regnefunksjoner.py ligger i samme
# mappe. Det samme gjelder forsaavidt for maal.txt for at filen skal kunne aapnes
from regnefunksjoner import tommerTilCm as ttc


# aapner en fil, leser linjene, legger til info i en ordbok og returnerer ordboken
def readFromFile():
    maal = {}
    f = open('maal.txt', 'r')

    for lines in f:
        a = lines.split(" ")
        maal[a[0]] = a[1][:-1:]

    f.close()

    return maal


def konverter(liste):
    konvertert = []
    for item in liste:
        # legger inn de koverterte verdiene inn i en ny liste
        konvertert.append(ttc(item))

    return konvertert


# legger til denne for at koden ikke skal kjøres dersom modulen blir importert
if __name__ == "__main__":

    # lagrer ordboken som returneres
    mine_maal = readFromFile()
    print (mine_maal)

    # lager en liste av noklene i ordboken
    keys = mine_maal.keys()

    # lager en liste av verdiene i ordboken som brukes som argument i
    # konverter-funksjonen
    verdier = konverter(mine_maal.values())

    print ("De konverterte verdiene er:")
    # itererer over begge listene samtidig og printer ut hvert ordnet par
    for item in zip(keys, verdier):
        print (f"{item}")
