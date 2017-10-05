""" Denne koden viser hvordan man legger til values og keys i en dictionary"""


# lager en ordbok med varer og priser
butikk = {"melk": 14.90, "brod": 24.90, "yoghurt": 12.90, "pizza": 39.90}

print (butikk)

# spør bruker om varenavn og pris to ganger. Legger disse inn i ordboken
while True:
    try:
        varenavn = input("Skriv inn ett varenavn: ")
        if varenavn == "":
            break
        pris = float(input("Srkiv inn prisen til varen: "))
        butikk[varenavn] = pris
    except ValueError:
        print ("Skriv inn rikitg pris! \n")
        continue

print (butikk)
print (sum(butikk.values()))
