wkt = 'MULTILINESTRING((0 0, 1 1), (1 1, 2 2, 3 3))'
multilinestring = []

# Remove the outer MULTILINESTRING parentheses
coords = wkt.replace('MULTILINESTRING', '').replace('(', '').replace(')', '')

# Split the string into individual LINESTRINGs
linestrings = coords.split(', ')

for linestring in linestrings:
    points = []
    # Split each LINESTRING into individual points
    coords = linestring.split(', ')
    for coord in coords:
        x, y = map(float, coord.split())
        points.append([x, y])
    multilinestring.append(points)

print(multilinestring)