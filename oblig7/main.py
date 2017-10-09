""" Bruker klassene til aa faa spillet til aa fungere """


from spillebrett import Spillebrett


def main():
    while True:

        # Ber bruker om rader og kolonner helt til riktig input
        try:
            rader = int(input("Skriv inn hvor mange rader du vil ha: "))
            kolonner = int(input("Skriv inn hvor mange kolonner du vil ha: "))

            if (rader <= 0) or (kolonner <= 0):
                print ("Oppgi positive heltall for baade kolonner og rader.")
                continue

            break

        except ValueError:
            print ("Oppgi et positivt heltall.")
            continue

    # Lager et spillebrett med brukerens input som parametre og tegner det.
    spillebrett = Spillebrett(rader, kolonner)
    spillebrett.tegnBrett()

    # Kjorer helt til bruker ber om avslutte.
    while True:

        svar = input("Trykk 'ENTER' for aa forsette eller 'q' for aa avslutte: ")

        if svar == "q":
            break
        elif svar == "":
            spillebrett.oppdatering()
            spillebrett.tegnBrett()
        else:
            print("Trykk enten 'ENTER' eller 'q'.")
            continue


main()
