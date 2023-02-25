# Import necessary modules and functions
import csv
from value_finder import points2invest


# Define constants and variables
CSV_FILE = 'matches.csv'
MONEY_LOW_ODD = 0
MONEY_HIGH_ODD = 0
MONEY_LOST = 0
MONEY_TOTAL_MADE = 0


# Open the CSV file and process the data
with open(CSV_FILE, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row if present
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Get the winning odd and two lowest odds
        odd_won = float(row[0])
        lowest_2_values = [float(x) for x in row[1].split(',')]
        
        # Calculate the investment points for the two lowest odds
        points_found = points2invest(lowest_2_values[0], lowest_2_values[1])
        
        # Invest the points and update the money variables
        # The third condition can change everything. If the distance between the two lowest odds is enough great:
        # then there is a win
        if points_found[0] != 0 and points_found[1] != 0 and lowest_2_values[1] - lowest_2_values[0] > 3.09:
            MONEY_LOW_ODD += points_found[0]
            MONEY_HIGH_ODD += points_found[1]
            
            if odd_won == lowest_2_values[0]:
                MONEY_TOTAL_MADE += points_found[0] * lowest_2_values[0]
            elif odd_won == lowest_2_values[1]:
                MONEY_TOTAL_MADE += points_found[1] * lowest_2_values[1]
            else:
                MONEY_LOST += points_found[0] + points_found[1]

# Print the results
print("Money low odd invested:", MONEY_LOW_ODD)
print("Money high odd invested:", MONEY_HIGH_ODD)
print("Money invested:", MONEY_LOW_ODD + MONEY_HIGH_ODD)
print("Money total made:", MONEY_TOTAL_MADE)
print("Money lost:", MONEY_LOST)
print("Final win:", round(MONEY_TOTAL_MADE - (MONEY_LOW_ODD + MONEY_HIGH_ODD),2))
