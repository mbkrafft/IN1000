""" Først defineres funksjonene minFunksjon og hovedprogram, så kjøres funksjonen hovedprogram. Inne i hovedprogramfunksjonen legges verdien 42 til variablen a og verdien 0 til variablen b. Så kjøres printfunksjonen med b som argument. b får deretter verdien som a peker til, og a får verdien som returneres av minFunksjon. Inne i minFunksjon blir en for-løkke opprettet som kjører to ganger. Gjennom første gjennomgang, hvor x = 0, blir c satt til verdien 2 og så sendt inn til printfunksjonen som argument. Deretter inkrementeres c med 1, slik at den får verdien 3. variablen b blir satt til verdien 10, for så å inkrementeres med verdien som a peker til. Problemet her er at a aldri har blitt definert inne i minFunksjon, og heller ikke har en global verdi. a peker derfor ikke til noen verdi. Dette gjør at programmet stoppes. """


def minFunksjon():
    for x in range(2):
        c = 2
        print (c)
        c += 1
        b = 10
        b += a
        print (b)
    return (b)


def hovedprogram():
    a = 42
    b = 0
    print (b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)


# legger til denne for at koden ikke skal kjøres dersom modulen blir importert
if __name__ == "__main__":
    hovedprogram()
