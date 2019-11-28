# This program drives a common cathode 7 segment display.
from gpiozero import LED
from time import sleep
# Set each led on the 7 segment with a unique gpio pin.
ledA = LED (10)
ledB = LED (22)
ledC = LED (27)
ledD = LED (17)
ledE = LED (4)
ledF = LED (6)
ledG = LED (13)

# Display 0 through 9 with a loop.
for count in range(11):
    if count == 0:
        # Turn on segment A,B,C,D,E,F to display 0 
        ledA.on()
        ledB.on()
        ledC.on()
        ledD.on()
        ledE.on()
        ledF.on()
        print("0")
        sleep(1)
        ledA.off()
        ledB.off()
        ledC.off()
        ledD.off()
        ledE.off()
        ledF.off()
    elif count == 1:
        # Turn on segment B and C to display 1.
        ledB.on()
        ledC.on()
        print("1")
        sleep(1)
        ledB.off()
        ledC.off()
    elif count == 2:
        # Turn on segment A, B, D, E, G to display 2.
        ledA.on()
        ledB.on()
        ledD.on()
        ledE.on()
        ledG.on()
        print("2")
        sleep(1)
        ledA.off()
        ledB.off()
        ledD.off()
        ledE.off()
        ledG.off()
    elif count == 3:
        # Turn on segment A, B, C, D, G
        ledA.on()
        ledB.on()
        ledC.on()
        ledD.on()
        ledG.on()
        print("3")
        sleep(1)
        ledA.off()
        ledB.off()
        ledC.off()
        ledD.off()
        ledG.off()
    elif count == 4:
        # Turn on segment F, B, C, G
        ledF.on()
        ledB.on()
        ledC.on()
        ledG.on()
        print("4")
        sleep(1)
        ledF.off()
        ledB.off()
        ledC.off()
        ledG.off()
    elif count == 5:
        # Turn on segment A, F, C, D, G
        ledA.on()
        ledF.on()
        ledC.on()
        ledD.on()
        ledG.on()
        print("5")
        sleep(1)
        ledA.off()
        ledF.off()
        ledC.off()
        ledD.off()
        ledG.off()
    elif count == 6:
        # Turn on segment A, F, E, C, D, G
        ledA.on()
        ledF.on()
        ledC.on()
        ledD.on()
        ledG.on()
        ledE.on()
        print("6")
        sleep(1)
        ledA.off()
        ledF.off()
        ledC.off()
        ledD.off()
        ledG.off()
        ledE.off()
    elif count == 7:
        # Turn on segment A, B, C
        ledA.on()
        ledB.on()
        ledC.on()
        print("7")
        sleep(1)
        ledA.off()
        ledB.off()
        ledC.off()
    elif count == 8:
        # Turn on segment A, B, C, D, E, F, G
        ledA.on()
        ledB.on()
        ledC.on()
        ledD.on()
        ledE.on()
        ledF.on()
        ledG.on()
        print("8")
        sleep(1)
        ledA.off()
        ledB.off()
        ledC.off()
        ledD.off()
        ledE.off()
        ledF.off()
        ledG.off()
    elif count == 9:
        # Turn on segment A, B, C, D, F, G
        ledA.on()
        ledB.on()
        ledC.on()
        ledD.on()
        ledF.on()
        ledG.on()
        print("9")
        sleep(1)
        ledA.off()
        ledB.off()
        ledC.off()
        ledD.off()
        ledF.off()
        ledG.off()
    else:
        print("End of count!")
        

        
