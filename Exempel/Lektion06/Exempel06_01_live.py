# Funktioner används för att separera och namnge en del av programmet, som
# ett eget litet miniprogram, så att man kan återanvända koden.
#
# I det här exemplet skriver vi en simpel funktion som skriver ut en
# hälsning på skärmen.

def hello_world():
    print("Hello, World!")


# Man kan också ge funktioner data som de behöver, i form av
# s.k. Argument, som då inte behöver delas i hela programmet.
#
# I det här exemplet accepterar vår funktion ett Argument, ett namn,
# som vi sen vill att funktionen ska hälsa på.

def hello(name):
    print("Hej ", name, "!", sep="")


# För att våra funktioner ska göra något så måste vi säga åt Python att faktiskt
# köra dem, ovan har vi bara berättat för Python vad namnen betyder.
hello_world()
hello("Johan")


# Funktioner kan också ge värden tillbaka, vilket man kallar
# att RETURNERA ett värde. De liknar på det sättet funktioner
# inom matematiken. Det returnerade värdet hamnar därefter på samma plats i
# koden som funktionsanropet skedde.
#
# I det här exemplet returnerar vi argumentet multiplicerat med två.
# Notera att det returnerade värdet nedan inte skrivs ut om vi inte skickar det
# vidare till print().

def f(x):
    return x * 2
# Exemplet ovan är t.ex. väldigt likt den matematiska funktionen f(x)=x*2


# Notera skillnaden på vad som händer på nedanstående rader.
f(3)
print(f(3))
dubblat = f(4)
print(dubblat)
f(8)
16
