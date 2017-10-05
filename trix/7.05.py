class EspressoMaskin:
    def __init__(self, vannmengde=0, navn="kaffemaskin uten navn"):
        self.vannmengde = vannmengde
        self.navn = navn

    # Lag espresso dersom det er nok vann
    def lag_espresso(self):
        if self.vannmengde > 40:
            self.vannmengde = self.vannmengde - 40
            print (f"Lager kaffe lungo, resterende vann i {self.navn} er naa {self.vannmengde} mL")
        else:
            print (f"Det er for lite vann igjen i {self.navn}. Kun {self.vannmengde} mL vann igjen")

    # Lag lungo dersom det er nok vann
    def lag_lungo(self):
        if self.vannmengde > 110:
            self.vannmengde = self.vannmengde - 110
            print (f"Lager kaffe lungo, resterende vann i {self.navn} er naa {self.vannmengde} mL")
        else:
            print (f"Det er for lite vann igjen i {self.navn}. Kun {self.vannmengde} mL vann igjen")

    # Fyll paa et gitt antall milliliter vann, dersom det er plass
    def fyll_vann(self, ml):
        if self.vannmengde + ml <= 1000:
            self.vannmengde = self.vannmengde + ml
            print (f"Det er naa {self.vannmengde} mL vann igjen i {self.navn}")
        else:
            print ("Du prover a fylle pa for mye vann")

    # Les av maalestrekene på vanntanken og tilgjengelig vann i ml
    def hent_vannmengde(self):
        print (f"Det er {self.vannmengde} mL igjen i {self.navn}")


kaffemaskin1 = EspressoMaskin(vannmengde=100, navn='kaffemaskin1')
kaffemaskin2 = EspressoMaskin(vannmengde=500, navn='kaffemaskin2')
kaffemaskin1.fyll_vann(20)
kaffemaskin1.lag_lungo()
kaffemaskin1.hent_vannmengde()
kaffemaskin1.lag_espresso()
kaffemaskin2.hent_vannmengde()
