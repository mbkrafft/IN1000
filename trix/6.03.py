def les_tall_liste():
    f = open('tall.txt', 'r')
    liste = []

    for line in f:
        # listelinjer kommer på formen '69\n'. Må derfor fjerne \n bak tallet for at
        # listen skal kun bestå av tall. Gjør så om typen fra string til heltall
        liste.append(int(line[0:len(line) - 1]))

    f.close()

    return liste


def antall_forekomster(liste, heltall):
    # teller forekomster av heltall i liste
    return liste.count(heltall)


def flest_forekomster(liste):
    flest = 0
    maxi = antall_forekomster(liste, liste[0])

    # Går gjennom alle tallene i listen og ser hvilket som forekommer flest.
    # Bruker set() for å slippe å gå igjennom det samme tallet flere ganger.
    for tall in set(liste):
        tmp = antall_forekomster(liste, tall)
        if tmp >= maxi:
            maxi = tmp
            flest = tall

    return flest


# Kan også gjøre det på denne måten. Key-argumentet bestemmer hvilken
# ting max() skal finne den største verdien av. I dette tilfellet
# finner vi hvilket tall som det er storst forekomster av.
# Grunnen til av vi bruker set() er for å slippe å se over like elementer
# flere ganger. set() gjor nemlig om listen til en mengde, og mengder inneholder
# ikke duplikater.
def flest_forekomster2(liste):
    return max(set(liste), key=liste.count)


liste = les_tall_liste()
tall = 15

print (liste)
print (f"Tallet {tall} forekommer {antall_forekomster(liste, tall)} ganger i dokumentet")
# OBS! Sjekker ikke om det er flere tall som forekommer like mange ganger. Disse to
# viser derfor ulike resultater.
print (f"Det tallet som forekommer flest ganger er {flest_forekomster(liste)}")
print (f"Det tallet som forekommer flest ganger er {flest_forekomster2(liste)}")
