# Original av: Henrik Tunedal
# Övning 06-03: Komplettera funktionen evaluate_temperature så att den
# returnerar lämpliga bedömningar, från fall till fall, av
# badtemperaturen som den får som argument. Bedömningen kan t.ex. vara
# "för kallt", "lagom" eller "för varmt".

# NOTERA: Det är ENDAST i funktionen evaluate_temperature som ni ska göra ändringar


def evaluate_temperature(degrees_celsius):
    return "av okänd badvänlighet"




# Allt efter denna rad ska vara oförändrat. Kommentarerna på följande rader
# finns enbart där för att förklara vad som händer.


def main():
    # Följande tre rader slumpar fram fem temperaturer så att vi testar om
    # funktionen klarar av både förutbestämda och slumpade temperaturer.
    from random import choices
    random_temp = choices(range(60), k=5)
    temperatures = [0, 25, 10, 50] + random_temp

    for temperature in temperatures:
        # Här anropar vi vår funktion evaluate_temperature och får
        # tillbaka en bedömning.
        assessment = evaluate_temperature(temperature)

        print("Vid", temperature, "grader anses badvattnet vara", assessment)


# Här anropar vi funktionen main. Namnet är konventionellt för den
# funktion där programmet tar sin början, men man kan egentligen kalla
# den vad man vill.
main()
