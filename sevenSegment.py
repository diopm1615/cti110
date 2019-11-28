# This program drives a 7 segment display.
import gpiozero
from time import sleep

ledA = LED (4)
ledB = LED (17)
ledC = LED (27)
ledD = LED (22)
ledE = LED (5)
ledF = LED (6)
ledG = LED (13)

# Display 0 through 9 with a loop.
for count in range(10):
    if count == 0:
        # Turn on segment A,B,C,D,E,F to display 0
        ledA.off() and ledB.off() and ledC.off() and ledD.off() and ledE.off() and ledF.off()
        pause(1) 
    elif count == 1:
        # Turn on segment B and C to display 1.
        ledB.off() and ledC.off()
        pause(1)
    elif count == 2:
        # Turn on segment A, B, D, E, G to display 2.
        ledA.off() and ledB.off() and ledD.off() and ledE.off() and ledG.off()
        pause(1)
    elif count == 3:
        # Turn on segment A, B, C, D, G
        ledA.off() and ledB.off() and ledC.off() and ledD.off() and ledG.off()
        pause(1)
    elif count == 4:
        # Turn on segment F, B, C, G
        ledF.off() and ledB.off() and ledC.off() and ledG.off()
        pause(1)
    elif count == 5:
        # Turn on segment A, F, C, D, G
        ledA.off() and ledF.off() and ledC.off() and ledD.off() and ledG.off()
        pause(1)
    elif count == 6:
        # Turn on segment A, F, E, C, D, G
        ledA.off() and ledF.off() and ledC.off() and ledD.off() and ledG.off() and ledE.off()
        pause(1)
    elif count == 7:
        # Turn on segment A, B, C
        ledA.off() and ledB.off() and ledC.off()
        pause(1)
    elif count == 8:
        # Turn on segment A, B, C, D, E, F, G
        ledA.off() and ledB.off() and ledC.off() and ledD.off() and ledE.off() and ledF.off() and ledG.off()
        pause(1)
    elif count == 9:
        # Turn on segment A, B, C, D, F, G
        ledA.off() and ledB.off() and ledC.off() and ledD.off() and ledF.off() and ledG.off()
        pause(1)

        