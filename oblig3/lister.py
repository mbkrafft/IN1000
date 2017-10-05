""" Denne koden viser mange av handlingene man kan gjøre med lister """

# legger til tall i en liste
liste = [2, 5, 6]

# legger til ett tall på slutten av en liste
liste.append(3)

# forsto oppgaveteksen sånn at dere ikke ber om indeks 1 og 3, men elementene
print (liste[0], liste[2])

# lager tom liste
nyliste = []

# spør om og legger til tekst i en liste
for i in range(4):
    tall = input("Skriv inn ett navn: ")
    nyliste.append(tall)

# sjekker om et spesifikt navn er i listen med navn
if "Mathias" in nyliste:
    print ("Du har husket meg!")
else:
    print ("Har du glemt meg?")

# legger sammen listene
sammenliste = liste + nyliste

print (sammenliste)

# sletter siste element i den sammenlagt listen
del sammenliste[len(sammenliste) - 1]
del sammenliste[len(sammenliste) - 1]

print (sammenliste)
