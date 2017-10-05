""" Skriv en klasse Person med en konstruktør som tar imot navn og alder. I tillegg skal konstruktøren ha en tom liste  hobbyer . Skriv en metode  leggTilHobby  som tar imot en tekststreng og legger den til i  hobbyer -listen. Skriv også en metode  skrivHobbyer.  Denne metoden skal skrive alle hobbyene etter hverandre på en linje. Gi deretter Person-klassen en metode  skrivUt  som i tillegg til å skrive ut navn og alder kaller på metoden  skrivHobbyer . La brukeren skrive inn navn og alder, og lag et Person-objekt med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal statistikk om brukeren skrives ut.
eren   skrives   ut. """


class Person:

    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

        self.hobbyer = []

    def leggTilHobby(self, hobby):
        self.hobbyer.append(hobby)

    def skrivUtHobbyer(self):
        for i in self.hobbyer:
            print (i)

    def skrivUt(self):
        print (self.navn)
        print (self.alder)
        print ("")
        print ("Hobbyer:")
        self.skrivUtHobbyer()


navn = input("Skriv et navn: ")
alder = input("Skriv en alder: ")

person1 = Person(navn, alder)

while True:
    svar = input("Legg til hobby eller skriv 'Q' for aa avslutte: ")

    if svar == "Q":
        break
    else:
        person1.leggTilHobby(svar)

person1.skrivUt()
