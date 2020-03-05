from datetime import date
year_of_birth = int(input("Enter your year of birth: "))
current_year = int(date.today().year)
current_age = current_year - year_of_birth
if current_age > 18:
    print("Congrats you are old enough")


