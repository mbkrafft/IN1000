def skriv_med_trykk(tekst=''):
    print(f"{tekst}!")


i = 0
while i < 5:
    uttrykk = input("Skriv noe du vil legge trykk på: ")
    if (uttrykk.lower() == "nei"):
        break
    skriv_med_trykk(uttrykk)
    i += 1
