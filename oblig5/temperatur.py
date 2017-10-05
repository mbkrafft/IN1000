""" Koden under viser hvordan man kan lese inn informasjon fra filer """

# en funksjon som leser inn en fil med gjennomsnittstemperatuer og returnerer
# en liste som inneholder disse temperaturene


def lesInnTemp():
    f = open('temperatur.txt', 'r')
    temp = []
    for lines in f:
        temp.append(int(lines))

    print (temp)

    f.close()

    return temp

# en funksjon som finner gjennomsnittsverdien av en liste


def average(liste):
    total = 0
    for item in liste:
        total = total + item

    return total / len(liste)


# legger til denne for at koden ikke skal kjøres dersom modulen blir importert
if __name__ == "__main__":
    temp = lesInnTemp()
    print (average(temp))
