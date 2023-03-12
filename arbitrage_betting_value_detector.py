import csv
import os

# This method is a private method to update the output.csv file with the extrapulated information
def _value_2_csv(filename, *args):
    with open(filename, 'a', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(args)
    

def _value_extractor(file_name):
    # Open the input and output files
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip first row
        row_count = 1

        for row in reader:
            row_count += 1
            values = row[1:]
            
            # Find the inconsistent blocks of values
            incons_blocks = [i for i, v in enumerate(values) if v != values[0]]
            
            if incons_blocks:
                # Compute the differences between adjacent values in each block
                block_diffs = [float(values[i]) - float(values[i + 2]) for i in range(0, len(values), 3)]
                
                # Sort the blocks based on their differences
                sorted_diffs_indices = sorted(range(len(block_diffs)), key=lambda k: block_diffs[k], reverse=True)
                
                # Get the values in the highest and lowest difference blocks
                sorted_diffs = sorted(block_diffs, reverse=True)
                first_diff = sorted_diffs[0]
                last_diff = sorted_diffs[-1]
                
                # Check if the blocks satisfy the arbitrage betting principle
                if first_diff * last_diff < 0:
                    # Update the output file with the relevant information
                    _value_2_csv("arbitrage_odds_to_calculate.csv", row[0], *values[sorted_diffs_indices[0]*3:(sorted_diffs_indices[0]+1)*3], *values[sorted_diffs_indices[-1]*3:(sorted_diffs_indices[-1]+1)*3])



def arbitrage_betting_final_odds_calculation():
    
    # Extract values from the input file and output the relevant information to a CSV file
    _value_extractor("games_with_all_odds.csv")
    
    
    with open(file="arbitrage_odds_to_calculate.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            home_odd = 0
            draw_odd = 0
            away_odd = 0
            
            if row[1] < row[3]:
                home_odd = row[4]
                away_odd = row[3]
            else:
                home_odd = row[1]
                away_odd = row[6]
            if row[2] < row[5]:
                draw_odd = row[5]
            else:
                draw_odd = row[2]
            
            _value_2_csv("final_output.csv", row[0], home_odd, draw_odd, away_odd)
            
arbitrage_betting_final_odds_calculation()
                
