# Lägg till en IF-sats så att greeting inte ändras.

we_want_to_mess_with_greeting = False
greeting = "Hej och tack! Jag blev inte borttagen!"
if we_want_to_mess_with_greeting == True:
    greeting = "Ånej! Jag blev ändrad!"

print(greeting)
