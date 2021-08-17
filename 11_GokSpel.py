

# we gaan een spelletje maken met een secret woord, die de geburiker kan kiezen
print("speel ons geheum woord spelletje")
secret_woord = "aap"
gok = ""

while gok != secret_woord:
    gok = input("waag een gok!: ")
print("je hebt gewonnen") #dit is de succes boodschaap

#we kunnen ook een limiet zetten, de gebruiker krijgt nu een limiet om goed te gokken, 3 kansnne

print("speel ons geheum woord spelletje, je hebt 3 kansen")
secret_woord = "aap"
gok = ""
#we gaan nu meer nformaite moeten bijhoude, eerst hoe vaak de gebruiker heeft gegokt..00000
gok_count = 0
#hier gaan we bijhouden hoevaak een gebruiker mag probeeren te gokken 22222
gok_limiet = 3
#dit is een boolean en dit gaat ons zeggen als de geburiekre geen gokken meer heeft 3333333
out_of_guesses = False

while gok != secret_woord and not(out_of_guesses): #5555 we gaan een dander condite hier toevoegen ,dus zolang ze het secret woord niet hebben en ze niet outof guesses zijn
    if gok_count < gok_limiet: #we willen weten als de gebruiker niet meer dan 3 keer gegeokt heeft 44444
        gok = input("waag een gok!: ")
        gok_count += 1 # dit gaam we optellen met 1 want we #1111
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("je hebt geen kansen meer, je verliest")
else:
    print("je hebt gewonnen") #dit is de succes boodschaap
