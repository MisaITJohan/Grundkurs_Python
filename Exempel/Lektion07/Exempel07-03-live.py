# Ett exempel på en "praktisk" användning av en inbyggd modul som måste
# importeras. Även ett exempel på varför det kan vara viktigt att följa
# stilregler.

#import random as ran
import random
from random import choices


my_card_list = ["Ruter Två", "Ruter Tre", "Ruter Fyra", "Ruter Fem",
                "Ruter Sex", "Ruter Sju", "Ruter Åtta", "Ruter Nio",
                "Ruter Tio", "Ruter Knekt", "Ruter Drottning",
                "Ruter Kung", "Ruter Äss", "Hjärter Två", "Hjärter Tre",
                "Hjärter Fyra", "Hjärter Fem", "Hjärter Sex", "Hjärter Sju",
                "Hjärter Åtta", "Hjärter Nio", "Hjärter Tio", "Hjärter Knekt",
                "Hjärter Drottning", "Hjärter Kung", "Hjärter Äss",
                "Klöver Två", "Klöver Tre", "Klöver Fyra", "Klöver Fem",
                "Klöver Sex", "Klöver Sju", "Klöver Åtta", "Klöver Nio",
                "Klöver Tio", "Klöver Knekt", "Klöver Drottning",
                "Klöver Kung", "Klöver Äss", "Spader Två", "Spader Tre",
                "Spader Fyra", "Spader Fem", "Spader Sex", "Spader Sju",
                "Spader Åtta", "Spader Nio", "Spader Tio", "Spader Knekt",
                "Spader Drottning", "Spader Kung", "Spader Äss"]

print("En slumpad dragning av fem spelkort:", choices(my_card_list, k=5))

print() # Tomt print() för att göra en tom rad.

# Vi skapar en ny lista och slumpar ordningen:
my_random_list = []

for card in my_card_list:
    my_random_list.append(card)

print("My card list:", my_card_list)
print()
print("My random list:", my_random_list)

print()
print()
x = random.shuffle(my_random_list) # Fel. 'x = ' ska inte vara där.
print(x)

print("My card list:", my_card_list)
print()
print("My random list:", my_random_list)
