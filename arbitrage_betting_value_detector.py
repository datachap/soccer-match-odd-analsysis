import csv

def value_extractor(file_name):
    with open(file_name, newline='') as csvfile, open("output.txt", 'w') as outfile:
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
                    outfile.write(f"Blocks at indices {sorted_diffs_indices[0] + 1} and {sorted_diffs_indices[-1] + 1}: {values[sorted_diffs_indices[0]*3:(sorted_diffs_indices[0]+1)*3]}, {values[sorted_diffs_indices[-1]*3:(sorted_diffs_indices[-1]+1)*3]}\n")

#TODO Add the part where it will give back the blocks and check then arbirtrage betting principle
value_extractor("games_with_all_odds.csv")
