import math

# Prompts user to choose calculation type
calculation_type = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n"
                         "investment - to calculate the amount of interest you'll earn on interest. \n"
                         "bond - to calculate the amount you'll have to pay on a home loan \n"
                         "(Investment, Bond): ")
# If user selects investment, prompt user for deposit amount, interest rate, investment years and type of interest
if calculation_type.lower() == "investment":
    deposit_amount = float(input("Enter the amount being deposited: R"))
    interest_rate = float(input("Enter the interest rate(%) figure: "))
    investment_years = int(input("How many years will you be investing for: "))
    interest = input("What type of interest do you require? (Compound, Simple): ")
# Calculate and print final payout rounded off to two decimal places based on the type of interest selected
    if interest.lower() == "simple":
        final_payout = deposit_amount * (1 + (interest_rate / 100) * investment_years)
        print("The final payout amount is R" + "{0:.2f}".format(final_payout))
    else:
        final_payout = deposit_amount * math.pow(1 + (interest_rate / 100), investment_years)  # format
        print("The final payout amount is R" + "{0:.2f}".format(final_payout))
# If user selects bond, prompt user for present value, interest rate and number of repayment months
else:
    present_value = float(input("Enter present value of the house: R"))
    monthly_interest_rate = float(input("Enter the interest rate(%): "))
    repayment_months = int(input("Enter the number of repayment months: "))

# Calculate and print monthly repayment rounded off to two decimal places
    monthly_repayment = present_value * ((monthly_interest_rate * (1 + monthly_interest_rate) ** repayment_months) / (
                ((1 + monthly_interest_rate) ** repayment_months) - 1))
    print("The monthly instalment amount to be paid is R" + "{0:.2f}".format(monthly_repayment))