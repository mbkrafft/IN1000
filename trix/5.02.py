def forekommer(tekst, tegn):

    if tegn in tekst:
        return True
    else:
        return False


def uten_repetisjon(tekst):
    # gjQr om tekstrengen til en mengde. Mengder har ingen repetisjoner
    a = (set(tekst))

    # returnerer elementene i mengden som en streng, uten noe mellom hvert
    # element
    return ''.join(a)


def antall_forskjellige(tekst):
    # returnerer lengden av teksten som ikke har noen reptisjoner
    return len(uten_repetisjon(tekst))


print (forekommer("inf1001", "i"))
print (uten_repetisjon("aababbabbac"))
print (antall_forskjellige("aababbabbac"))
