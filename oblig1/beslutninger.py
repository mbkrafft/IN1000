""" Dette programmet spør brukeren om de har lyst på en brus og svarer
tilbake basert på hva brukeren skrev. """

# ber brukeren om et svar på om de vil ha brus
svar = input("Kunne du tenkt deg en brus? (ja/nei): ")

# gir svar basert på hva brukeren skrev
if svar == "ja":
    print ("Her har du en brus!")
elif svar == "nei":
    print ("Den er grei.")
else:
    print ("Det forstod jeg ikke helt.")
