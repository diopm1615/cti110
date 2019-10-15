#CTI-110
#P4HW2-MealTipTax 
#Mame Diop
#14/10/2019
#

# This program will calculate the total amount of a meal purchased at a restaurant.
# Create a variable to control the loop.
calculateAnotherMeal = "y"
while calculateAnotherMeal.lower() == "y":

    # Get the foodcharge and tip.
    foodCharge = float(input("Please enter the charge for food: "))    
    tip = float(input("Please enter the tip for the server: "))

    # Prevent the user from entering a wrong tip with a loop.
    while tip != 0.16 and tip != 0.18 and tip != 0.20:
        print("Error tip must be .16 or .18 or .20")
        tip = float(input("Please enter the tip for the server(must be .16 0r .18 or .20): "))

    # Calculate tip amount, tax amount and total cost of food.   
    tipAmount = (foodCharge * tip)
    taxAmount = (foodCharge * 0.06)
    totalFoodCharge = (foodCharge + tipAmount + taxAmount)

    # Display original food charge, tip amount, tax amount and total cost of food.
    print("The original food amount is: $", foodCharge, sep="")
    print("Your tip amount is: $",format(tipAmount, ".2f" ), sep="")
    print("Your tax amount is: $", format(taxAmount, ".2f"), sep="")
    print("Your total cost of meal is: $", format(totalFoodCharge, ".2f"), sep="")

    # Ask the user if he/she wants to calculate another food charge.
    calculateAnotherMeal = input("do you want to calculate another meal and enter a new tip: (y/n)")

print("Have a good day.")

input()
