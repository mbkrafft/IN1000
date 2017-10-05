""" Lager en prosedyre som tar inn navn og bosted. Disse printes ut
som en hilsen. Kjører så prosedyren tre ganger"""


# lager prosedyre
def utskriftsprosedyre():
    navn = input("Skriv inn navn: ")  # tar inn navn fra brukeren
    bosted = input("Hvor bor du? ")  # tar inn bosted fra brukeren
    print (f"Hei, {navn}! Du er fra {bosted}.")  # skriver ut info


# kjører prosedyren tre ganger
utskriftsprosedyre()
utskriftsprosedyre()
utskriftsprosedyre()
