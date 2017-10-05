""" Koden viser hvordan while-løkker kan brukes. Sorterer så listen som blir laget."""

liste = []

# While-løkke som kjører helt til bruker taster inn 0.
while True:
    try:
        tall = int(input("Skriv inn et heltall: "))
    except ValueError:
        print ("Ikke skriv inn noe annet enn et heltall.")
        continue

    if tall == 0:
        break

    liste.append(tall)

# Skriver ut alle verdiene i listen
for item in liste:
    print (item)

# Summerer alle verdiene i listen og skriver ut resultatet
minSum = 0
for item in liste:
    minSum = minSum + item
print (minSum)


# Finne minste tall i listen
tmp_min = liste[0]
for tall in liste:
    if tall < tmp_min:
        tmp_min = tall
print (tmp_min)

# Finner største tall i listen
tmp_max = liste[0]
for tall in liste:
    if tall > tmp_max:
        tmp_max = tall
print (tmp_max)
