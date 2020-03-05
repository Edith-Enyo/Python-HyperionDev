# declare variables and assign values to each variable
print("Logical Programming Task 1")
num1 = int(21)
num2 = int(15)
num3 = int(40)


# compare values, determine maximum print  maximum of both values
if num1 > num2:  # can we use this as well? print(max(num1, num2))
    print(num1)
else:
    print(num2)

# using the modulus function,check if num1 is divisible by 2, if yes, it is an even, if no it is an odd number
if (num1 % 2) == 0:
    print("num1 is an even number")
else:
    print("num1 is an odd number")

# Sort numbers descending order using conditional statements
# Large
if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3
# Middle
if (num2 < num1) and (num1 < num3):
    middle = num1
elif (num1 < num2) and (num2 < num3):
    middle = num1
else:
    middle = num3
# Small
if (num1 < num2) and (num2 < num3):
    small = num1
elif(num2 < num1) and (num1 < num3):
    small = num2
else:
    small = num3
# Display Results
print("The numbers in descending order are: " + str(largest) + "," + str(middle) + "," + str(small))
