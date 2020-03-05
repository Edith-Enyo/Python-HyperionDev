# Prompt user to enter weight and height
weight = float(input("Please enter your weight in Kgs:"))
height = float(input("Please enter your height in meters:"))
# Calculate BMI based on the weight and height details
BMI = float(weight/(height*height))
# Display obese, overweight, normal or underweight based on user's BMI
if BMI >= 30:
    print("Your BMI is " + str(BMI) + ". You are obese.")
elif BMI >= 25:
    print("Your BMI is " + str(BMI) + ". You are overweight.")
elif BMI >= 18.5:
    print("Your BMI is " + str(BMI) + ". Your weight is normal.")
else:
    print("Your BMI is " + str(BMI) + ". You are underweight")