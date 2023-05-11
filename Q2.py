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

import requests

# Set the API endpoint and parameters
endpoint = "https://maps.googleapis.com/maps/api/directions/json"
params = {
    "origin": "Canberra",
    "destination": "Barton",
    "mode": "transit",
    "transit_mode": "bus",
    "key": "AIzaSyAzmIkaPnXXghoAImiCqL1wlYW5shytqKE"
}

# Send a request to the API endpoint with the specified parameters
response = requests.get(endpoint, params=params)

# Parse the JSON response
data = response.json()

# Extract the bus route and time data
legs = data["routes"][0]["legs"][0]
route = legs["arrival_time"]["text"]
time = legs["duration"]["text"]

# Print the extracted data
print("Bus route:", route)
print("Bus travel time:", time)
