""" Lager en klasse Motorsykkel, samt forskjellige metoder som tilhorer klassen """


class Motorsykkel:

    def __init__(self, merke, regnummer, km):
        self.merke = merke
        self.regnummer = regnummer
        self.km = int(km)

    def kjor(self, km):
        self.km += km

    def hentKilometerAvstand(self):
        return f"{self.merke}'en har naa kjort {self.km} km"

    def skrivUt(self):
        print (f"Motorsykkelen med merke {self.merke} og registreringsnummer {self.regnummer} har kjort {self.km} kilometer.")
