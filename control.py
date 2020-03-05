from datetime import date
# Prompt user to enter age
age = int(input("How old are you: "))
# Base of age range, print old enough, almost there or you are just too young
if age >= 18:
    print("You are old enough!")
elif 16 < age < 18:
    print("Almost there")
else:
    print("You're just too young")