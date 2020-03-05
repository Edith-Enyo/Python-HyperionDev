# Import math to use maths functions, i.e. Pi
import math
math.pi
print("Area covered by a foundation of a building")

# Prompt user for inputs
building_shape = input("Enter shape of building:(Square, Round, Rectangular): ")
# Calculate and display dimension using the formula length to the power of 2  if foundation is square.
if building_shape.lower() == "square":
    area_of_square = float(input("Please enter the appropriate dimensions: "))
    area_of_foundation = area_of_square ** 2
    print(str("Area taken by foundation of the building is " + str(area_of_foundation)))
# Calculate and display dimension using the formula length x width if foundation is rectangular.
if building_shape.lower() == "rectangle":
    width = float(input("Please enter the width of building: "))
    length = float(input("Please enter the length of the building: "))
    area_of_foundation = width * length
    print(str("Area taken by foundation of the building is " + str(area_of_foundation)))
# Calculate and display dimension using the formula 𝛱radius 2 if foundation is round.
if building_shape.lower() == "round":
    radius = float(input("Please enter the radius of the foundation: "))
    area_of_foundation = float(math.pi * (radius**2))
    print("Area taken by foundation of the building is " + str(area_of_foundation))
