""" Lager en spillebrettklasse med ulike metoder """


from random import randint
from celle import Celle


class Spillebrett:

    def __init__(self, rader, kolonner):

        self.rader = rader
        self.kolonner = kolonner
        self.rutenett = []
        self.generasjonsnummer = 0

        # For hver rad, lager en ny liste. For hver kolonne i hver rad, legger
        # til et nytt celleobjekt.
        for i in range(self.rader):
            self.rutenett.append([])
            for j in range(self.kolonner):
                self.rutenett[i].append(Celle())

        # Kaller pa generermetoden for aa legge til status for alle celler paa
        # spillebrettet
        self.generer()

    def tegnBrett(self):
        for i in range(self.kolonner):
            for j in range(self.rader):
                # finner tegn til hver celle. Skriver ut uten ny linje, ved
                # hjelp av keyword agrument end=" ", som gir kun et mellomrom
                # som avslutning paa print()
                print (self.rutenett[j][i].hentStatusTegn(), end=" ")
            print ("")

        print(f"Generasjon: {self.generasjonsnummer}\nAntall levende: {self.finnAntallLevende()}")

        print("\n")

    def oppdatering(self):

        dod_til_levende = []
        levende_til_dod = []

        # gaar gjennom hver celle, rad for rad, fra overst venstre
        for i in range(self.kolonner):
            for j in range(self.rader):

                # finenr alle naboer til den naavaerende cellen
                naboliste = self.finnNaboListe(i, j)

                # Sjekker hvor mange antall levende naboer cellen har
                antall_levende_naboer = 0
                for item in naboliste:
                    if item is True:
                        antall_levende_naboer += 1

                # bestemmer cellens neste status
                if self.rutenett[j][i].erLevende() == True:
                    if not ((antall_levende_naboer == 2) or (antall_levende_naboer == 3)):
                        levende_til_dod.append(self.rutenett[j][i])
                else:
                    if (antall_levende_naboer == 3):
                        dod_til_levende.append(self.rutenett[j][i])

        for celle in dod_til_levende:
            celle.settLevende()

        for celle in levende_til_dod:
            celle.settDoed()

        self.generasjonsnummer += 1

    def finnAntallLevende(self):

        antall_levende = 0

        for i in range(self.kolonner):
            for j in range(self.rader):
                if self.rutenett[j][i].erLevende() is True:
                    antall_levende += 1

        return antall_levende

    def generer(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                rand = randint(0, 3)
                if rand == 3:
                    self.rutenett[i][j].settLevende()

    def finnNaboListe(self, x, y):

        naboliste = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                naboX = x + i
                naboY = y + j
                if ((naboX == x) and (naboY == y)) != True:
                    if ((naboX < 0) or (naboY < 0) or (naboX > self.kolonner - 1) or (naboY > self.rader - 1)) != True:
                        # legger returverdien til erLevende() inn i listen
                        naboliste.append(self.rutenett[naboY][naboX].erLevende())

        return naboliste
