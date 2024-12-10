# Demander à l'utilisateur une année
year = int(input("Please type in a year: "))

# Vérification des règles des années bissextiles
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")