import csv

with open('stops.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('stopDict.txt', 'w') as txt_file:
        for row in csv_reader:
            bus_stop_dict = {'stop_id': int(row['stop_id']), 'stop_code': row['stop_code'], 'stop_name': row['stop_name'], 'stop_lat': float(row['stop_lat']), 'stop_lon': float(row['stop_lon']), 'zone_id': row['zone_id'], 'stop_url': row['stop_url'], 'location_type': int(row['location_type']), 'wheelchair_boarding': int(row['wheelchair_boarding'])}
            txt_file.write(str(bus_stop_dict) + '\n')