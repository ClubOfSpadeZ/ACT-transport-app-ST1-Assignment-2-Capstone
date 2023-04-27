import json

# Open the JSON file and read its contents
with open('Bus_Routes.json') as f:
    data = json.load(f)

# Get the WKT data
wkt = data['route'][0][8]

# Remove the outer MULTILINESTRING parentheses
coords = wkt.replace('MULTILINESTRING', '').replace('(', '').replace(')', '')

# Split the string into individual LINESTRINGs
linestrings = coords.split(', ')

# List to store the multilinestring data
multilinestring = []

for linestring in linestrings:
    points = []
    # Split each LINESTRING into individual points
    coords = linestring.split(', ')
    for coord in coords:
        x, y = map(float, coord.split())
        # Append each point as a dictionary
        points.append({"lat": y, "lng": x})
    # Append each LINESTRING as a list of points
    multilinestring.append(points)

print(multilinestring)