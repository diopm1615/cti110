
# This is a program that will calculate and display the annual profit made from the projected amount of total sales.
# 09/15/2019
# CTI-110 P2T1 - Sales Prediction
# Mame Diop
#

projected_amount_of_total_sales = float(input("Please enter the projected amount of total sales: " ))    # get the projected amount of total sales.

annual_profit = projected_amount_of_total_sales * 0.23                                                   # calculate the annual profit.

print ("The annual profit that will be made is: $", format(annual_profit, ',.2f'), sep="")               # display the annual profit with 2 digit after the decimal point

input()


