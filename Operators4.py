# Prompt user for input
integer = int(input("Enter an integer: "))
# Determine and display if integer is divisible by 2 and 5
if (integer % 2) == 0 and (integer % 5) == 0:
    print("Integer: " + str(integer) + ",  is divisible by 2 and 5")
else:
    print("Integer: " + str(integer) + ", is not divisible by 2 and 5")
# Determine and display if integer is divisible by 2 or 5
if (integer % 2) == 0 or (integer % 5) == 0:
    print("Integer: " + str(integer) + ",  is divisible by 2 or 5")
else:
    print("Integer: " + str(integer) + ", is not divisible by 2 or 5")
# Determine and display if integer is not divisible by 2 or 5
if (integer % 2) != 0 or (integer % 5) != 0:
    print("Integer: " + str(integer) + ",  is not divisible by 2 or 5")
else:
    print("Integer: " + str(integer) + ", is divisible by 2 or 5")
