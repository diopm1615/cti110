# This program counts the total of collected bugs for 7 days.
# 10/10/2019
# CTI-110 P4T2 - Bug Collector
# Mame Diop
#

# Initialize the bug counter.
bugCount = 0

# Get the number of captured bug each days for 7 days.
for day in range(1, 8):
    bug = int(input("Enter the number of bugs collected for day " + str(day) + ": "))
    
    # Count the total of bugs.
    bugCount += bug

print()

# Print the total of bugs collected.
print("The total of bugs collected in 7 days are: ",bugCount)

input()
