""" Lager en celleklasse som brukes for aa representere cellene i spillet. """


class Celle:

    #   Constructor
    def __init__(self):
        self.status = self.settDoed()
        self.tegn = self.hentStatusTegn()

    def settDoed(self):
        self.status = "dod"
        return self.status

    def settLevende(self):
        self.status = "levende"
        return self.status

    def erLevende(self):
        if self.status == "levende":
            return True
        elif self.status == "dod":
            return False
        else:
            raise ValueError

    def hentStatusTegn(self):
        if self.erLevende() is True:
            self.tegn = "O"
        else:
            self.tegn = "."
        return self.tegn
