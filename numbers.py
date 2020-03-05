# Prompt user to enter 3 different numbers
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
# Calculate total of all 3 numbers
print("\nSum of all three inputs")
sum_numbers = num1+num2+num3
print(sum_numbers)
# The first number minus the second number
print("\nFirst number minus the third number")
subtraction_function = num1 - num2
print(subtraction_function)
# The third number multiplied by the first number
print("\nThird number multiplied by the first number")
multiplication_function = num3*num1
print(multiplication_function)
# The sum of all three numbers divided by the third number
print("Sum of all three numbers divided by third number")
sum_average = sum_numbers/num3
print(sum_average)


