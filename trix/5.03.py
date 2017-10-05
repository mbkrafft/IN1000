tall = int(input("skriv inn et heltall: "))
liste = [x for x in range(2, tall, 1)]


def sjekk_om_primtall(tall, liste):

    sjekk = tall - 1

    # går gjennom alle tall (sjekk) mindre enn input (tall) og sjekker
    # om noen av de er delelig med input
    while sjekk > 1:
        # hvis rest er lik null, finnes det et delelig tall mindre enn input
        if tall % sjekk == 0:
            return False

        sjekk -= 1

    # hvis vi kommer hit, vet vi at tallet er et primtall
    return True


print (sjekk_om_primtall(tall, liste))
