# Prompt user to enter names of all pupils in a class and store it in a list called names
names = ""
# set the counter to zero
i = 0
# Using a while loop's repetitive properties, prompt user to enter names
# when user types stop, system calculates and prints number of names typed
while names != "stop":
    names = input("Please enter the names of all pupils in the class  list : ").lower()
    if names != "stop":
        i += 1
print(i)


