# Loopar kan innehålla if-satser eller andra loopar

my_int = 1
my_second_int = 10


while my_int < my_second_int:
    if my_int % 2 == 0:
        print(my_int)
    else:
        print("Här är ett udda tal!")
        
    my_int = my_int + 1

    
print("Här är loopen över!")
