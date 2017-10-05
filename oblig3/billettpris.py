""" Denne koden lager en prosedyre som gir billettpriser utifra alderen brukeren
taster inn. """


def pris():

    # tar inn alder
    alder = int(input("Hva er alderen din? "))

    billettpris = 0

    # sjekker hvor gammel brukeren sier den er og gir billettpris utifra dette
    if alder <= 17:
        billettpris = 30
    elif 17 < alder:
        billettpris = 50
    elif 63 < alder:
        bilettpris = 35

    print(f"Din alder er {alder}, saa du maa betale {billettpris},-")


for i in range(4):
    pris()

# Det er en logisk feil i prosedyren. Pensjonistbilletter vil aldri bli
# komme til, ettersom vi ikke avgrenser hvor høyt opp alder skal gå på
# den normale billetten.
