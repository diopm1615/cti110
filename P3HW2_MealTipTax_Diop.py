#This program will calculate the total amount of a meal purchased at a restaurant.
#CTI-110
#P3HW2-MealTipTax 
#Mame Diop
#09/25/2019
#


foodCharge = float(input("Please enter the charge for food: "))                      # get the cost of the food before tip and tax.

tip = float(input("Please enter the tip for the server: "))                          # get the tip for the server.

if tip == 0.16:
    tipAmount = (foodCharge * 0.16)                                                  # Calculate the tip amount.
    taxAmount = (foodCharge * 0.06)                                                  # Calculate the tax amount.
    totalFoodCharge = (foodCharge + tipAmount + taxAmount)                           # Calculate the total cost of meal.
    print("The original food amount is: $", foodCharge, sep="")                      # Display the original food amount.
    print("Your tip amount is: $",format(tipAmount, ".2f" ), sep="")                 # Display the tip amount.
    print("Your tax amount is: $", format(taxAmount, ".2f"), sep="")                 # Display the tax amount.
    print("Your total cost of meal is: $", format(totalFoodCharge, ".2f"), sep="")   # Display the total cost of meal.

elif tip == 0.18:
    tipAmount = (foodCharge * 0.18) 
    taxAmount = (foodCharge * 0.06)
    totalFoodCharge = (foodCharge + tipAmount + taxAmount)                           # Calculate the total cost of meal.
    print("The original food amount is: $", foodCharge, sep="")                      # Display the original food amount.
    print("Your tip amount is: $", format(tipAmount, ".2f"), sep="")                 # Display the tip amount.
    print("Your tax amount is: $", format(taxAmount, ".2f"), sep="")                 # Display the tax amount.
    print("Your total cost of meal is: $", format(totalFoodCharge, ".2f"), sep="")   # Display the total cost of meal.
elif tip == 0.20:
    tipAmount = (foodCharge * 0.20)
    taxAmount = (foodCharge * 0.06)
    totalFoodCharge = (foodCharge + tipAmount + taxAmount)                           # Calculate the total cost of meal.
    print("The original food amount is: $", foodCharge, sep="")                      # Display the original food amount.
    print("Your tip amount is: $", format(tipAmount, ".2f"), sep="")                 # Display the tip amount.
    print("Your tax amount is: $", format(taxAmount, ".2f"), sep="")                 # Display the tax amount.
    print("Your total cost of meal is: $", format(totalFoodCharge, ".2f"), sep="")   # Display the total cost of meal.
else:
    print("You entered a wrong tip")                                                 # Display an error if the tip entered is not 16% 0r 18% or 20%.

input()

      
