import csv

# File path
file_path = 'csvfile.csv'

# Initialize total sum variable
total_sum = 0

# Open the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Loop through each row
    for row in reader:
        try:
            total_sum += float(row[0])  # Sum the value in the first column
        except ValueError:
            print(f"Invalid value found: {row[0]}. Skipping.")

print("Sum of values in the first column:", total_sum)