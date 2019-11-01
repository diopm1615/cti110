# This program adds or substracts two random numbers and ask the user to guess the result.
# 11/01/2019
# CTI-110 P5HW2 - Math Quiz
# Mame Diop
#

import random

# set the constant for the main menu choices.
addRandNum = 1
subsRanNum = 2
Exit = 3

# Define the main function.
def main():

    # Set the initial choice to run the program and control the loop.
    choice = 0

    while choice != Exit:

        # Display the menu.
        menuChoice()

        # Ask the user to make a choice to do the math quiz or quit the program.
        choice = int(input("Do you want to guess the answer of a math quizz: "))
        print()

        # Perform the choice selected.
        if choice == addRandNum:
            addition()
        
        elif choice == subsRanNum:
            substraction()

        # Quit the program if the user chooses to quit.
        elif choice == Exit:
            input("Exiting the program......")
            
        # Let the user know if the choice is not play game nor exit.
        else:
            print("Error: invalid entry")
            print()
        




# Define the function menuChoice().
def menuChoice():
    print()
    print("---------------------")
    print("......MAIN MENU......")
    print("1) Add Numbers")
    print("2) Substract Numbers")
    print("3) Exit")
    print("---------------------")

# Define the function addition().
def addition():

    # Generate two random numbers.
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)

    # Add the two random numbers and assign the 
    # result the variable "result".
    result = num1 + num2
    
    # Display the two random numbers.
    print()
    print(" ", num1 )
    print("+", num2)
    print("-----")
    print()

    # Get the user answer.
    userAnswer = int(input("Please enter you answer: "))
    
    # Compare the result and the user answer.
    if result == userAnswer:
        # Display a congratulation message.
        print()
        print("Congratulation,",result,"is the right answer.")

    else:
        # Display a message telling the user his answer's wrong.
        print()
        print("Sorry your answer is incorrect.",
        result,"was the correct answer.")
        print()

# Define the function substraction().
def substraction():

    # Generate two random numbers.
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)

    # Substract the two random numbers and assign the 
    # result the variable "result".
    result = num1 - num2
    
    # Display the two random numbers.
    print()
    print(" ", num1)
    print("-", num2)
    print("-----")
    print()

    # Get the user answer.
    userAnswer = int(input("Please enter you answer: "))
    
    # Compare the result and the user answer.
    if result == userAnswer:
        # Display a congratulation message.
        print()
        print("Congratulation,",result,"is the right answer.")

    else:
        # Display a message telling the user his answer's wrong.
        print()
        print("Sorry your answer is incorrect.",
        result,"was the correct answer.")
        print() 

main()       





