# Exempel på hur man kan importera funktioner från andra
# moduler och hur man refererar till dem i koden.

import tobeimported_live

# Variabeln __name__ får olika värden beroende på vilken
# fil man startade programmet ifrån. Den modulen blir då
# "the main module", huvudmodulen.

print("Från Exempel07_01:", __name__)
print("tobeimported_live ifrån Exempel07_01_live:",
      tobeimported_live.__name__)

print()
if __name__ == '__main__':
    print("Exempel07_01_live är main")
