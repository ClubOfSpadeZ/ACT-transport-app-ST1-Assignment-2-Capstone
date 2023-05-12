import csv
import requests


def stop_name(stop_id):
    with open('static\data\stops.csv', 'r') as file:

        # Create a CSV reader object
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Iterate over each row in the CSV file
        for row in reader:
            if row[0] == str(stop_id):
                name = row[2]

                return name


def main(stop_1 : str, stop_2 : str, key:str):
    # Set the API endpoint and parameters
    endpoint = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": stop_name(stop_1),
        "destination": stop_name(stop_2),
        "mode": "transit",
        "transit_mode": "bus",
        "optimize": "true",
        "key": key
    }

    response = requests.get(endpoint, params=params)

    data = response.json()

    if data["status"] != "OK":
        print("Error:", data["status"])
    else:
        if len(data["routes"]) > 0:
            fastest_time = data["routes"][0]["legs"][0]["duration"]["text"]
            return fastest_time
        else:
            fastest_time = "No routes found"
            return fastest_time


