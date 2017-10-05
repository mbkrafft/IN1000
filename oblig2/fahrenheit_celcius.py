""" verktøy for å konvertere en gitt temperatur fra fahrenheit til celcius."""


# tar inn temp i fahrenheit
fahrenheit = float(input("Hvor mange grader i fahrenheit er det?\n>"))

# skriver ut temp i fahrenheit
print (f'{fahrenheit} grader fahrenheit')

# konverterer temp til celcius
celcius = (fahrenheit - 32) * (5 / 9)

# skriver ut temp i celcius
print (f'{round(celcius, 2)} grader celcius')
