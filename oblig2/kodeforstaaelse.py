"""
1.
Nei. Man kan ikke legge sammen to forskjellige typer. b er et heltall,
mens "Hei!" er tekst.

2.
Går utifra at oppgaven mener at man har rettet opp i feilen med
forskjellige typer som legges sammen -> str(b) i printfunksjonen.
Isåfall vil man få disse problemene:
* Dersom bruker taster inn noe annet enn tall, vil ikke int() funksjonen kunne
gjøre om teksten til et heltall.
* Dersom tallet som blir tastet inn er 10 eller mer vil ingenting skje.
"""

# Kode
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
