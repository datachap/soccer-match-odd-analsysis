
import csv
from value_finder import points2invest

with open('matches.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row if present
    # invested money
    money_low_odd = 0
    money_high_odd = 0
    
    money_lost = 0
    money_total_made = 0
    
    for row in reader:
        odd_won = float(row[0])
        
        lowest_2_values = [float(x) for x in row[1].split(',')]
        points_found = points2invest(lowest_2_values[0], lowest_2_values[1])
        money_low_odd += points_found[0]
        money_high_odd += points_found[1]
        
        
        if odd_won == lowest_2_values[0]:
            print ("Lowest odd")
            money_total_made += points_found[0] * lowest_2_values[0]
        elif odd_won == lowest_2_values[1]:
            print ("Highest odd")
            money_total_made += points_found[1] * lowest_2_values[1]
        else:
            print("Money loss")
            money_lost += points_found[0] + points_found[1]

    print (money_low_odd)
    print (money_high_odd)
    print ("Money invested: " + str(money_low_odd + money_high_odd))
    print (money_total_made)
    print (money_lost)
    print ("Final win: " + str(money_total_made - (money_low_odd + money_high_odd)))