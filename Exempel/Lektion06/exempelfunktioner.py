# Exempel på hur man definierar, skapar, egna funktioner:


# def för att meddela att vi DEFINIERAR vad en ny funktion betyder.
# Namnet på funktionen. Bör vara lätt att förstå och BÖR inte innehålla åäö. Namnet
# bör också vara i små bokstäver med understreck(_) istället för mellanslag.
# Parenteser, (). För att de MÅSTE vara där även om vi inte planerar att använda
# argument med denna funktion.
# Ett kolon, :, för att påbörja själva definitionen.
# En indentering på alla rader som tillhör funktionen.

def exempelfunktion():
    print("Vår funktion gör inget för stunden så jag lägger in lite text så länge.")


# När vi vill köra vår funktion, även kallat för att 'anropa' eller 'kalla' på den, så
# måste vi använda parenteser, (), efter namnet för att meddela att vi faktiskt vill
# köra funktionen.
exempelfunktion()


# Om vi vill skapa en funktion som ska kunna ta emot instruktioner om vad den
# ska arbeta med så måste vi skriva in det innanför parenteserna när vi
# DEFINIERAR vår funktion.
# T.ex. vilken text som ska skrivas ut av print() eller vilka tal som ska
# läggas ihop av en funktion som adderar två tal.
def funktion_som_tar_emot_tre_argument(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3):
    print(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3)

# Det som vi skriver inom parenteserna i DEFINITIONEN är alltså vad vi namnger
# det som skickas till vår funktion som argument varje gång den körs.


funktion_som_tar_emot_tre_argument(8, "HEJ", 4.567)
funktion_som_tar_emot_tre_argument(4.567, godtyckligt_namn3=5, godtyckligt_namn2="HEJ")
funktion_som_tar_emot_tre_argument(6, 7)

x = 42
funktion_som_tar_emot_tre_argument(x, x, x)
# Nästa rad kommer att krascha programmet.
print(godtyckligt_namn1)
