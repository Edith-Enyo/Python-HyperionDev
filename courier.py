# Declare variables for each factor and assign values specifies to it
Air = float(0.36)
Freight = float(0.250)
full_insurance = float(50)
limited_insurance = float(25)
gift_package = float(15)
normal_package = float(0)
priority_delivery = float(100)
standard_delivery = float(20)
# This variable will be used to determine the final cost
deliv_Cost = float(0)

# Ask the user to enter the price of package and distance in kms
package_price = float(input("Enter price of package you would like to purchase: "))
distance = float(input("Enter total distance of delivery in kms: "))

# Prompt user to enter required options and prints their prices
courier_type = input("What type of service do you require? (Air or Freight)")
if courier_type.lower() == "air":
    print("Air delivery cost is R0.36")
    deliv_Cost += Air*distance
else:
    print("Freight delivery cost is R0.25")
    deliv_Cost += Freight*distance

insurance_type = input("What insurance option do you require?(Full or Limited)")
if insurance_type.lower() == "full":
    print("Full insurance costs R50")
    deliv_Cost += full_insurance
else:
    print("Limited insurance costs R25")
    deliv_Cost += limited_insurance

gift_type: str = input("Is this a gift item? (Yes or No)")
if gift_type.lower() == "yes":
    print("Gift packages cost R15")
    deliv_Cost += gift_package
else:
    deliv_Cost += normal_package

delivery_type = input("Is this a priority delivery item? (Yes or No)")
if delivery_type.lower() == "yes":
    print("Priority delivery costs R100")
    deliv_Cost += priority_delivery
else:
    print("Standard deliveries cost R20")
    deliv_Cost += standard_delivery
# Add package price to the true variables and prints the total cost of product
total_cost = float(deliv_Cost + package_price)
print("The total cost of the product equals " + str(total_cost))