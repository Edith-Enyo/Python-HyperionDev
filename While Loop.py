# Prompt user to enter a number and store in a list called num
num = ""
# Set counter, sum values and average to zero
count = 0
sum_of_inputs = 0
average = 0
# Using a while loop's repetitive properties, prompt user to enter a number until user enters -1
while num != -1:
    num = int(input("Enter a number: "))
    if num != -1:
        count += 1
        sum_of_inputs += num
# If number entered is -1, system calculates and prints average of all numbers entered
    else:
        average = sum_of_inputs/count
        # print("The average of the numbers entered is:" + str(average))
        print("The average of the numbers entered is:" + "{0:.2f}".format(average))

