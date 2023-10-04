# Vi skriver lite funktioner tillsamans:


# def för att meddela att vi DEFINERAR vad en ny funktion betyder.
# Namnet på funktionen bör vara lätt att förstå och BÖR inte innehålla åäö. Namnet
# bör också vara i små bokstäver med understeck (_) istället för mellanslag.
# Parenteser, (), för att de MÅSTE vara där även om vi inte planerar att använda
# argument med denna funktion.
# Kolon, :, för att påbörja själva definitionen.
# En indentering på allt som funktionen ska göra.
def exempelfunktion():
    print("Vår funktion gör inget för stunden så jag lägger in lite text så länge.")

# När vi vill köra vår funktion, även kallat för att anropa eller kalla på den, så
# måste vi använda parenteser, (), efter namnet för att meddela att vi faktiktiskt
# vill köra funktionen.
exempelfunktion()


# Om vi vill skriva en funktion som ska kunna ta emot instruktioner om vad den
# ska arbeta mes så måste vi skriva in det innanför parenteserna när vi
# DEFINERAR vår funktion.
# T.ex. vilken text som ska skrivas ut av print() eller vilka tal som ska
# läggas ihop av en funktion som adderar två tal.
def funktion_som_tar_emot_tre_argument(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3):
    print(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3)

# Det som vi skrev inom parenteserna i DEFINITIONEN är alltså vad vi namnger
# det som skickats till vår funktion som argument.

funktion_som_tar_emot_tre_argument(8, "HEJ", 4.567)
