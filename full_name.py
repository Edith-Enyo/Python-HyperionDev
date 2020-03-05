# Prompt user to enter full name
user_name = input("Enter your full name: ")

# Validate to ensure user enters an input
if len(user_name) == 0:
    print("You haven’t entered anything. Please enter your full name.")

# Validate to ensure full name is not less than 4 characters
elif len(user_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.");

# Validate to ensure full name is not more than 25 characters
elif len(user_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name");

# If all validations pass, print out Thank you for entering your name
else:
    print("Thank you for entering your name.")

