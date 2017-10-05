"""
Quiztid!
Svar riktig på spørsmålene og se hvor mange riktige svar du får. Du får tre
poeng for riktig svar, men minus ett poeng for feil svar. Blanke svar gir null poeng.

a) Initialiser poengsum og skriv en velkomst til terminalen.

b) Be om svar av brukeren til følgene spørsmål:
1. Hvilken verdenskjent artist ville ha fylt 59 år i dag, hadde det ikke vært for at han døde i 2009?
riktig svar -> michael jackson
2. Hvilket dyr omhandler Alfred Fidjestøls nye biografi, Nesten menneske?
riktig svar -> julius
3. Hva heter den foreløpig siste James Bond-filmen?
riktig svar -> spectre
4. Til hvilken ordklasse hører ordet nokså?
riktig svar -> adverb
5. Hvor mye veier en bikolibri, som er verdens minste fugleart? (i gram)
riktig svar -> 2

c) For hvert svar brukeren gir, sjekk om svaret er riktig, blankt eller feil. Oppdater poengsummen,

d) Skriv ut poengsummen underveis og til slutt ut den endelige poengsummen, sammen med en gratulasjon.
"""

poeng = 0
print("Velkommen til quiz.")

svar = input(
    "1. Hvilken verdenskjent artist ville ha fylt 59 år i dag, hadde det ikke vært for at han døde i 2009?\n>")
if svar.lower() == "michael jackson":
    poeng = poeng + 3
elif svar == "":
    pass
else:
    poeng = poeng - 1
print(f'du har {poeng} poeng!')

svar = input("2. Hvilket dyr omhandler Alfred Fidjestøls nye biografi, Nesten menneske?\n>")
if svar.lower() == "julius":  # sjimpansen fra Kristiansand Dyrepark
    poeng = poeng + 3
elif svar == "":
    pass
else:
    poeng = poeng - 1
print(f'du har {poeng} poeng!')

svar = input("3. Hva heter den foreløpig siste James Bond-filmen?\n>")
if svar.lower() == "spectre":
    poeng = poeng + 3
elif svar == "":
    pass
else:
    poeng = poeng - 1
print(f'du har {poeng} poeng!')

svar = input("4. Til hvilken ordklasse hører ordet nokså?\n>")
if svar.lower() == "adverb":
    poeng = poeng + 3
elif svar == "":
    pass
else:
    poeng = poeng - 1
print(f'du har {poeng} poeng!')

svar = input("6. Hvor mye veier en bikolibri, som er verdens minste fugleart? (i antall gram)\n>")
if svar.lower() == "2":
    poeng = poeng + 3
elif svar == "":
    pass
else:
    poeng = poeng - 1
print(f'du har {poeng} poeng!')

print(f'Gratulerer du fikk {poeng} poeng!')


""" Kunne også brukt funksjon for å slippe å gjenta beslutningslogikken """
# def sjekkriktigsvar(svar, riktig, poeng):
#     if svar.lower() == riktig:
#         poeng = poeng + 3
#     elif svar == "":
#         pass
#     else:
#         poeng = poeng - 1
#
#     print(f'du har {poeng} poeng!')
#     return poeng
#
#
# poeng = 0
# print("Velkommen til quiz.")
#
# svar = input(
#     "1. Hvilken verdenskjent artist ville ha fylt 59 år i dag, hadde det ikke vært for at han døde i 2009?\n>")
# poeng = sjekkriktigsvar(svar, "michael jackson", poeng)
#
# svar = input("2. Hvilket dyr omhandler Alfred Fidjestøls nye biografi, Nesten menneske?\n>")
# poeng = sjekkriktigsvar(svar, "julius", poeng)
#
# svar = input("3. Hva heter den foreløpig siste James Bond-filmen?\n>")
# poeng = sjekkriktigsvar(svar, "spectre", poeng)
#
# svar = input("4. Til hvilken ordklasse hører ordet nokså?\n>")
# poeng = sjekkriktigsvar(svar, "adverb", poeng)
#
# svar = input("6. Hvor mye veier en bikolibri, som er verdens minste fugleart? (i antall gram)\n>")
# poeng = sjekkriktigsvar(svar, "2", poeng)
