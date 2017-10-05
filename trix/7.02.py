class Bil:

    def __init__(self, eier="Ingen", merke="Generisk merke"):
        self.eier = eier
        self.merke = merke

    def skriveUt(self):
        print (f"{self.eier} eier en {self.merke}")


a = Bil(eier="Jens", merke="BMW")
b = Bil(eier="Mats", merke="Golf")

b.skriveUt()
a.skriveUt()
