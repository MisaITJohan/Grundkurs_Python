# Funktioner (också kallade procedurer eller subrutiner) används
# för att separera och namnge en del av programmet, som ett eget
# litet miniprogram, så att vi kan återanvände den.
#
# I det här exemplet skriver vi en simpel funktion som skriver
# ut en hälsning på skärmen.

def hello_world():
    print("Hello World")


# Man kan också ge funktionen data som den behöver, i form av
# s.k. argument, som då inte behöver delas i hela programmet.
#
# I det här exemplet accepterar vår funktion ett argument, ett namn,
# som vi vill att programmet ska hälsa på.


def hello(name):
    print("Hej ",name,"!",sep="")


# Funktioner kan också ge värden tillbaka, vilket man kallar
# att returnera ett värde. De liknar på det sättet funktioner
# inom matematiken.
#
# I det här exemplet returnerar vi argumentet multiplicerat med två,
# d.v.s. att vi dubblar det första värdet.

def f(x):
    return x * 2



hello_world()
hello("Johan")
hello("Sirpa")
f(23)   # Denna rad syns inte när vi kör programmet iom att det
        # returneras till detta fönster.
