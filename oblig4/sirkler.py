""" Benytter while-løkke for å lage animasjon med ezgraphics. """

from ezgraphics import GraphicsWindow

# lager vindu og lerret
win = GraphicsWindow()
can = win.canvas()

# setter variabler
storrelse = 20
teller = 0
x_pos = 10

while teller < 9:
    # tegner med de fortløpende oppdaterte variablene
    can.drawOval(x_pos, 100, storrelse, storrelse)

    # oppdaterer variabler
    x_pos += 5
    storrelse += 5
    teller += 1

# holder vinduet åpent
win.wait()
