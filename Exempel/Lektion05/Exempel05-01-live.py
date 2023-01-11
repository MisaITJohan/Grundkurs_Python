# Demonstration av slicing på listor och strängar.

my_fruit_list = ["Päron", "Äpplen", "Apelsiner", "Citroner", "Vindruvor"]

# Jag hämtar och skriver ut de tre första elementen ur my_fruits_list på
# två olika sätt.
print(my_fruit_list[0:3])
print(my_fruit_list[:3])

# Jag gör detsamma med de tre elementen i mitten.
print(my_fruit_list[1:4])

# Slutligen, de tre sista elementen. På tre olika sätt.
print(my_fruit_list[2:5])
print(my_fruit_list[2:])
print(my_fruit_list[-3:])

# Slicing fungerar även på strängar.
print("123456789"[0:5])