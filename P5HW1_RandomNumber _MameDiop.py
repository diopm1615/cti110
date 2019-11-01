# This program generates a random number and ask the user to guess it.
# 10/30/2019
# CTI-110 P5HW1 - Random Number
# Mame Diop
#

import random

# Set the constants for the menu choices.
playGame = 1
exit = 2

# Define the main function.
def main():

    # Set the initial choice to run the program and control the loop.
    choice = 0

    while choice != exit:

        # Display the menu.
        menuChoice()

        # Ask the user to make a choice to play or quit the program.
        choice = int(input("Do you want to play the game 'Guess The Number': "))
        print()

        # Perform the choice selected.
        if choice == playGame:

            # Generate a random number between 1 to 100.
            numGenerated = random.randint(1, 101)


            # Set a counter for the number of guesses.
            countGuess = 0

            # Start the loop.
            while countGuess != -1:

                # Ask the user to guess a number from 1 to 100
                # and set a counter for the number of guesses.
                guess = int(input("please guess a number from 1 to 100: "))
                print()
                countGuess += 1

                # Set a control condition that ask the user if to continue
                # playing after 10 guesses or go back to the main menu.
                if countGuess == 10:
                    askUser = input("You made 10 wrong guesses! Do you want to continue guessing: (y/n)")
                    print()
                    if askUser.lower() == "y":
                        print("Ok!")
                        print()
                        countGuess = 0

                    # Warn the user if he doesn't enter y or n.
                    elif askUser.lower() != "y" and askUser.lower() != "n":
                        print("Error: invalid entry")
                        break
                        
                    else:
                        print("Going to the main menu....")
                        break
                    
                else:
                    # Compare the generated number and the user number and display the result.
                    if guess > numGenerated:
                        print("Too high, try again")
                        print()
                            
                        
                    elif guess < numGenerated:
                        print("Too low guess again")
                        print()
                            

                    else:
                        print("Congratulation!",guess, "was the right number and you made",countGuess,"guesses.")
                        break
               
                        

        # Quit the game if the user chooses to quit.
        elif choice == exit:
            input("Exiting the program......")
            
        # Let the user know if the choice is not play game nor exit.
        else:
            print("Error: invalid entry")
            print()

        

# Define the function menuChoice().
def menuChoice():
    print()
    print("....MENU....")
    print("1) Play game")
    print("2) Exit")
    print("------------")
    print()

main()
