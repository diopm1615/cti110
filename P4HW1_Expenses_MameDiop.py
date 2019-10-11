# CTI-110
# P4HW1 - Expenses
# Mame Diop
# 10/10/2019

# This program calculates an user expenses.

# Initialize a counter for the number of expenses entered.
numberOfExpense = 1

# Create a variable to control the loop.
anotherExpense = "y"

# Get the amount in account in which money will be withdraw.
amountInAccount = float(input("Please enter the amount in your account: "))
print()

# Create a variable for the total of the expenses.
totalOfExpense = 0

# Start the loop.
while anotherExpense.lower() == "y":

    # Get the expense.
    expense = float(input("Please enter expense " + str(numberOfExpense) + " :"))
    print()

    # Calculate the total of expenses.
    totalOfExpense = totalOfExpense + expense

    # Update the number of expense counter.
    numberOfExpense = numberOfExpense + 1

    # Ask the user if he wants to enter another expense.
    anotherExpense = input("Do you want to enter another expense: (y/n)")
    print()


    

    


# Display the amount in account before expense.
print("The amount on your account before any expense was: $",
format(amountInAccount, ",.2f"), sep="")
print()

# Display the number of expense entered and the total of the expenses.
print("You entered ", numberOfExpense-1 , " expense(s) for a total of $",
      format(totalOfExpense, ",.2f"), sep="")
print()

# Calculate the amount remaining in account after expense.
remainInAccount = amountInAccount - totalOfExpense

# Display the remaining amount in account.
print("The amount remaining in your account is $", 
format(remainInAccount, ",.2f"), sep="")

input()





