""" Leser fra fil og gir statistikk utifra dette """


def innlesning(filnavn):
    f = open(filnavn, "r")
    statistikk = {}

    # for hver linje i filen, legger til hva som er foran mellomrommet inn som
    # nokkel og hva som er etter mellomrommet som verdi i ordboken statistikk
    for lines in f:
        statistikk[lines.split(" ")[0]] = int(lines.split(" ")[1])

    f.close()

    return statistikk


def maanedensAnsatt(ordbok):
    # lager lister over baade verdier og nokler i ordboken
    verdier = list(ordbok.values())
    nokler = list(ordbok.keys())

    # max(verdier) gir den storste verdien i listen over verdier.
    # verdier.index(stortsverdi) gir indexen til den verdien som er storst
    # i listen over verdiene.
    # Bruker indexen til aa gi hvilken nokkel som har denne verdien
    storstverdi = max(verdier)
    storstnokkel = nokler[verdier.index(storstverdi)]

    print (f"Maanedens ansatt er {storstnokkel} med {storstverdi} salg.")


def totaltAntallSalg(ordbok):
    verdier = list(ordbok.values())

    return (sum(verdier))


def aktiveSelgere(ordbok):
    nokler = list(ordbok.keys())

    return len(nokler)


def gjennomsnittSalg(ordbok):
    return round(float(totaltAntallSalg(ordbok)) / float(aktiveSelgere(ordbok)), 2)


def hovedprogram():
    ordbok_fra_fil = innlesning("fil.txt")

    maanedensAnsatt(ordbok_fra_fil)
    print ("")
    print (f"Aktive selgere denne maaneden: {aktiveSelgere(ordbok_fra_fil)}")
    print (f"Totalt antall salg: {totaltAntallSalg(ordbok_fra_fil)}")
    print (f"Gjennomsnittlig antall salg per salgsperson: {gjennomsnittSalg(ordbok_fra_fil)}")


hovedprogram()
