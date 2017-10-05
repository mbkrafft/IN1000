""" Lager en hundeklasse med forskjellige metoder. Ser ogsaa at instansvariablene kan
bli satt som baade parametre naar init blir kjort og som fast variabel """


class Hund:

    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10

    def hentAlder(self):
        return self.alder

    def hentVekt(self):
        return self.vekt

    def spring(self):
        self.metthet -= 1

        if self.metthet < 5:
            self.vekt -= 1

    def spis(self, mat=0):
        self.metthet += int(mat)

        if self.metthet > 7:
            self.vekt += 1
