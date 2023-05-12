import csv

def data(route):
    with open('Bus_Routes.csv', 'r') as file:

        # Create a CSV reader object
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Iterate over each row in the CSV file
        for row in reader:
            if row[4] == str(route):
                coords = row[0]

    return coords

