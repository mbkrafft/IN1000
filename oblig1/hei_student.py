""" Dette programmet skriver ut 'Hei Student!' til terminalen.
Brukeren blir så bedt om å oppgi ett navn. Etter dette blir 'Hei' 
og navnet som ble oppgitt printet ut til terminalen. """

# skriver ut 'Hei Student!' til terminalen
print ("Hei Student!")

# lagrer en input tekststring til variabelen "navn"
navn = input("Oppgi ett navn: ")

# printer ut "Hei" etterfulgt av den tekststringen som variablen navn peker til
print (f'Hei {navn}')
