""" Denne koden tegner en rød sirkel. """

# importerer GraphicsWindowklassen fra ezgraphicsmodulen
from ezgraphics import GraphicsWindow

# lager et vindu
win = GraphicsWindow()

# lager et kanvass i vinduet
can = win.canvas()

# spesiferer fargen til sirkelen
sirkel = can.setColor("red")

# tegner sirkelen
sirkel = can.drawOval(150, 150, 50, 50)

# holder vinduet åpent
win.wait()
