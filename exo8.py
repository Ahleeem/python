# Demander un nombre entier à l'utilisateur
number = int(input("Number: "))

# Vérifier les conditions pour Fizz, Buzz ou FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    pass  # Pas