# Module 5 Lab-5 Bottle Return Program
# Jarrod Saffioti
# 03/06/2024
# This program counts the amount of bottles received by a store and the subsequent payout.

# Declare variables
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"
NBR_OF_DAYS = 8 #Counter starts at 1, so this has to be 1 higher as well
PAYOUT_PER_BOTTLE = .10

# Loop to run program again
while counter <= NBR_OF_DAYS:
    today_bottles = int(input('Enter number of bottles returned for day #' + str(counter) + ": "))
    total_bottles += today_bottles
    counter += 1

    if counter == NBR_OF_DAYS:
        #Calculations
        total_payout = total_bottles * PAYOUT_PER_BOTTLE

        #Output
        print('The total number of bottles collected is', total_bottles)
        print(f'The total paid out is $ {total_payout:.1f}')
        keep_going = input('\n\nDo you want to enter another week\'s worth of data?\n(Enter y or n): ')

        #Restart sequence
        if keep_going == "y":
            total_payout = 0 #resets to 0 for multiple runs
            total_bottles = 0 #resets to 0 for multiple runs
            counter = 1 #resets to 1 for multiple runs
            continue
        else:
            break
        
