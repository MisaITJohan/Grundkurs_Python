# Funktioner används för att separera och namnge en del av programmet, som
# ett eget litet miniprogram, så att man kan återanvända koden.
#
# I det här exemplet skriver vi en simpel funktion som skriver ut en hälsning
# på skärmen.
def hello_world():
    print("Hello, World!")


# Man kan också ge funktioner data som de behöver, i form av s.k. arguemnt,
# som då inte behöver delas i hela programmet.
#
# I det här exemplet accepterar vår funktion ett argument, ett namn,
# som vi vill att programmet ska hälsa på.
def hello(name):
    print("Hej ", name, "!", sep="")


# Funktioner kan också ge värden tilbaka, vilket man kallar
# att RETURNERA ett värde. De liknar på det sättet funktioner
# inom matematiken.
#
# I det här exemplet returnerar vi argumentet multiplicerat med två.
# Notera att det returnerade värdet nedan inte skrivs ut om vi inte skickar
# det vidare till print().

def f(x):
    return x * 2
# Exemplet ovan är t.ex. väldigt likt den matematiska funktionen f(x)=x*2


hello_world()
hello("Johan")
print()

print(f(3))
dubblat = f(4)
print(dubblat)
f(8)
16
print()

print("Skriver ut värdet som returneras av print:", print("Inre print"))
x = print("Lagrar print:s returvärde i x")
print("Värdet på x är:", x)


# Vi lagrar resultatet av f(1) i f_av_ett
f_av_ett = f(1)
# Vi tar resultatet från förra raden, skickar det till f och lagrar
# resultat på nytt i en ny variabel.
f_av_f_av_ett = f(f_av_ett)

print("Vad är", f_av_f_av_ett)
