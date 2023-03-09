import csv

# All the constants used
FILE_NAME = "games_with_all_odds.csv"


def value_exctractor():
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        row_count = 0
        for row in csv_reader:
            row_count += 1
            if row:  # Skip empty rows
                values = [float(x) for x in row[1:] if x]  # Convert non-empty strings to floats
                block_count = 0
                for i in range(0, len(values), 3):
                    block_count += 1
                    block = values[i:i+3]
                    if len(block) == 3:
                        if block[0] < block[2]:
                            print(f"Row {row_count}, block {block_count}: First value is smaller than third value: {block}")
                        elif block[0] > block[2]:
                            print(f"Row {row_count}, block {block_count}: First value is greater than third value: {block}")
                        else:
                            print(f"Row {row_count}, block {block_count}: First and third values are equal: {block}")
                    else:
                        print(f"Row {row_count}, block {block_count}: Incomplete block: {block}")


value_exctractor()