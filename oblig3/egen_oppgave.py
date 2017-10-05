""" Tegner opp en figur basert på info brukeren gir """

# Oppgavetekst:
# Skriv   et   program   som   tar   imot   koordinater   samt   høyde   og
# bredde   fra bruker,   legger   disse   etter   hverandre   i   en   liste
# og   deretter   bruker   innholdet   i   listen   til   å tegne   opp   en
# form   med   EzGraphics.

# importerer GraphicsWindowklassen fra ezgraphicsmodulen
from ezgraphics import GraphicsWindow

# plasserer info i en liste
liste = []

# tar inn brukerinfo
typ = input("Skriv inn hvilken type figur('oval' eller 'rektangel'): ")
liste.append(int(input("Skriv inn x-koordinat: ")))
liste.append(int(input("Skriv inn y-koordinat: ")))
liste.append(int(input("Skriv inn hoyde: ")))
liste.append(int(input("Skriv inn bredde: ")))


# lager vindu og kanvass
win = GraphicsWindow()
can = win.canvas()

# tegner figur med info hentet ut fra listen
if typ == "oval":
    oval = can.drawOval(liste[0], liste[1], liste[2], liste[3])
elif typ == "rektangel":
    rekt = can.drawRectangle(liste[0], liste[1], liste[2], liste[3])
else:
    tekst = can.drawText(150, 150, "Skriv rikitg figur!")
    # holder vinduet åpent
win.wait()
