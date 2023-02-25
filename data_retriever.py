
import csv

with open('file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row if present
    for row in reader:
        odd_won = float(row[0])
        lowest_2_values = [float(x) for x in row[1].split(',')]
        if odd_won == lowest_2_values[0]:
            print(f"{odd_won} is the first value in {lowest_2_values}")
        elif odd_won == lowest_2_values[1]:
            print(f"{odd_won} is the second value in {lowest_2_values}")
        else:
            print(f"{odd_won} is not in {lowest_2_values}")