import csv

# All the constants used
FILE_NAME = "games_with_all_odds.csv"
OUTPUT_FILE = "output.txt"

def value_extractor():
    with open(FILE_NAME, newline='') as csvfile, open(OUTPUT_FILE, 'w') as outfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip first row
        row_count = 1

        for row in reader:
            row_count += 1
            values = row[1:]
            incons_blocks = [i for i, v in enumerate(values) if v != values[0]]
            if incons_blocks:
                block_diffs = [float(values[i]) - float(values[i + 2]) for i in range(0, len(values), 3)]
                sorted_diffs_indices = sorted(range(len(block_diffs)), key=lambda k: block_diffs[k], reverse=True)

                sorted_diffs = sorted(block_diffs, reverse=True)
                first_diff = sorted_diffs[0]
                last_diff = sorted_diffs[-1]
                if first_diff * last_diff < 0:
                    outfile.write(f"The row with an incosistency is: {row_count}\n")
                    outfile.write(f"First and last value of block diffs: {first_diff}, {last_diff}\n")
                    outfile.write(f"First and last index: {sorted_diffs_indices[0] + 1 }, {sorted_diffs_indices[-1] + 1}\n")
                    outfile.write(f"Block indices sorted by difference: {[i + 1 for i in sorted_diffs_indices]}\n")


value_extractor()
