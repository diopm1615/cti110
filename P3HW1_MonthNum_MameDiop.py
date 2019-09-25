# This program ask the user to enter a number from 1 to 12 and match that number
# with the month it represents.
# CTI-110
# P3HW1 - Month number
# Mame Diop
# 09/25/19
#

# Get the user number and compare that number with the number representing
# the month and display the name of the month's number that was entered.
# If the number is outside of the range 1 through 12 display an error message.
userNumber = int(input("Please enter the month's number: "))

if userNumber == 1:
    print("Your number represent January.")
elif userNumber == 2:
    print("Your number represent February.")
elif userNumber == 3:
    print("Your number represent March.")
elif userNumber == 4:
    print("Your number represent April.")
elif userNumber == 5:
    print("Your number represent May.")
elif userNumber == 6:
    print("Your number represent June.")
elif userNumber == 7:
    print("Your number represent July.")
elif userNumber == 8:
    print("Your number represent August.")
elif userNumber == 9:
    print("Your number represent Septembre.")
elif userNumber == 10:
    print("Your number represent October.")
elif userNumber == 11:
    print("Your number represent Novembre.")
elif userNumber == 12:
    print("Your number represent December.")
else:
    print("you made an error the number should be through 1 to 12.")

input()
