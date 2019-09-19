
#This program will calculate the total amount of a meal purchased at a restaurant.
#09/15/2019
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Mame Diop
#

food_charge = float(input("Please enter the charge for food: "))                       # get the cost of the food before tip and tax.

tip = float(input("Please enter the tip for the server: "))                            # get the tip for the server in decimal number.

tax = float(input("Please enter the tax rate: "))                                      # get the tax rate in decimal number.

tip_amount = food_charge * tip                                                         # calculate the tip amount.

tax_amount = food_charge * tax                                                         # calculate the tax amount.

total_amount = food_charge + tip_amount + tax_amount                                   # calculate the total cost of the food.

print("The total amount of the meal is: $", format(total_amount, (",.2f")), sep=(""))  # display the total amount of the meal with two number after the decimal point.


input()
      
