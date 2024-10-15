import csv

with open("analyze_results.csv", "w", newline="\n") as analyze_results_file:
    writer = csv.writer(analyze_results_file)

    writer.writerow(["A", "B"])

    with open("dataset.csv", "r") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)
        _, _, initial_A, initial_B = map(float, next(reader))

        prev_dried_A = initial_A
        prev_dried_B = initial_B

        for line in reader:
            absorbed_A, absorbed_B, dried_A, dried_B = map(float, line)

            if absorbed_A == -1 or absorbed_B == -1:
                continue

            delta_A = absorbed_A - prev_dried_A
            delta_B = absorbed_B - prev_dried_B

            prev_dried_A = dried_A
            prev_dried_B = dried_B

            writer.writerow([round(delta_A, 2), round(delta_B, 2)])

        
    
