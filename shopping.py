# Prompt user to enter names of three products
product1 = input("Enter the name of a product: ")
product2 = input("Enter the name of a second product:")
product3 = input("Enter the name of the third product: ")
# Prompt user to enter price of each item
product1_price = int(input("Enter the price of the first product: "))
product2_price = int(input("Enter the price of the second product: "))
product3_price = int(input("Enter the price of the third product:"))
# Calculate total of all three products
print("Total of all three products")
sum_of_products = product1_price+product2_price+product3_price
print(sum_of_products)
# Calculate average of all three products
print("Average of all three products")
average_of_products = sum_of_products/3
print(average_of_products)
print("The Total of " + product1 + "," + product2 + "," + product3 + " is R" + str(sum_of_products) + " and the average price of the items are R" + str(average_of_products))
