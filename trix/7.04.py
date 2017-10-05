class Rektangel:

    def __init__(self, lengde, bredde):
        self.lengde = lengde
        self.bredde = bredde

    def ok_lengde(self, oklengde):
        self.lengde = self.lengde + oklengde

    def ok_bredde(self, okbredde):
        self.bredde = self.bredde + okbredde

    def areal(self):
        return self.lengde * self.bredde

    def omkrets(self):
        return (2 * self.lengde) + (2 * self.bredde)

    def red_lengde(self, redlengde):
        self.lengde = self.lengde - redlengde

    def red_bredde(self, redbredde):
        self.lengde = self.lengde - redbredde


rek1 = Rektangel(10, 10)
rek2 = Rektangel(20, 20)

print (rek1.areal(), rek2.areal())

rek1.ok_lengde(20)
rek2.ok_bredde(20)

print (rek1.areal(), rek2.areal())
print (rek1.omkrets(), rek2.omkrets())
