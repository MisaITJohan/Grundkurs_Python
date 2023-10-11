# Första gången vi importerar en modul i vårt program laddas
# den från disk och koden i modulen körs.
print("Importar modulen tobeimported...")
import tobeimported_live
print("Importerad modul:", tobeimported_live)

# Observera att koden i tobeimported_live inte körs andra gången,
# om vi importerar modulen igen eftersom vi har laddat den tidigare.

print()
print("Importerar samma modul igen!")
import tobeimported_live
print("Fortfarande samma modul:", tobeimported_live)
