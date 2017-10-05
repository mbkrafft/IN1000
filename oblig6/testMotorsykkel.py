""" Tester om klassen motorsykkel fungerer som den skal """


from motorsykkel import Motorsykkel


def hovedprogram():
    mc1 = Motorsykkel("Honda", "KJ1245", "100")
    mc2 = Motorsykkel("Yamaha", "SI1235", "50")
    mc3 = Motorsykkel("Kawasaki", "SA1234", "0")

    mc1.skrivUt()
    mc2.skrivUt()
    mc3.skrivUt()

    mc3.kjor(10)
    print (mc3.hentKilometerAvstand())


hovedprogram()
