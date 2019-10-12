# This program will print a raw of ashtags separated by spaces.
# 10/11/19
# CTI-110 P4HW3 - Nested Loops
# Mame Diop
#
# This is how this program's going to work: the outer loop's going to iterate  
# 6 times. At each iteration the inner loop's going to old the value from 0 to 5
# and create 0 spaces all the way to 5 spaces. The outer will then print the 
# second ashtag.

for r in range(6):                  # Display 6 row of ashtags.
    print("#", end="", sep="")      # Display the first ashtag on each row
    for c in range(r):              
        print(" ",end="",sep="")    # Create the space between ashtags for each iteration of the outer loop
    print("#", sep="")              # Display the second ashtag on each row
   
    
input()   

    

    
