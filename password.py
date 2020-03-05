# Declare boolean variables
have_length = False
up_case = False
low_case = False
have_num = False

# this variable will be used to count the number of correct characteristics
trueVariablesCheck = 0

# Check password length is at least 6 characters
lengthCheck = input("Is the password entered at least 6 characters long? (Yes or No)")
if lengthCheck.lower() == "yes":
    have_length = True
    trueVariablesCheck += 1

# Check password contains an upper case
uppercaseCheck = input("Does your password contain upper case letters? (Yes or No)")
if uppercaseCheck.lower() == "yes":
    up_case = True
    trueVariablesCheck += 1

# Check password contains an lower case
lowCaseCheck = input("Does your password contain lower case letters? (Yes or No)")
if lowCaseCheck.lower() == "yes":
    low_case = True
    trueVariablesCheck += 1

# Check password contains numbers
numberCheck = input("Does your password contain numbers? (Yes or No)")
if numberCheck.lower() == "yes":
    have_num = True
    trueVariablesCheck += 1

# Print suitable characteristic if the number of suitable characteristics equals 3
if trueVariablesCheck >= 3:
    print("Password is suitable")

# This was not asked but if suitable characteristics is less than 3,this line prompts user to enter a suitable password
else:
    print("Please enter a suitable password")