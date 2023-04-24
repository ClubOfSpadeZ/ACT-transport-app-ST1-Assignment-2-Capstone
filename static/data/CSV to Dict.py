# import csv
#
# with open('stops.txt') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     with open('stopDict.txt', 'w') as txt_file:
#         for row in csv_reader:
#             bus_stop_dict = {'stop_id': int(row['stop_id']), 'stop_code': row['stop_code'], 'stop_name': row['stop_name'], 'stop_lat': float(row['stop_lat']), 'stop_lon': float(row['stop_lon']), 'zone_id': row['zone_id'], 'stop_url': row['stop_url'], 'location_type': int(row['location_type']), 'wheelchair_boarding': int(row['wheelchair_boarding'])}
#             txt_file.write(str(bus_stop_dict) + '\n')

import xml.etree.ElementTree as ET
import json

# parse the XML file
tree = ET.parse('Bus_Stops.xml')
root = tree.getroot()

# create an empty dictionary to hold the data
data = {}

# iterate over the XML nodes and extract the data
for row in root.findall('./row/row'):
    stop_id = row.find('stop_id').text
    stop_latitude = row.find('stop_latitude').text
    stop_longitude = row.find('stop_longitude').text
    stop_name = row.find('stop_name').text
    suburb = row.find('suburb').text
    location = row.find('location')
    location_latitude = location.get('latitude')
    location_longitude = location.get('longitude')
    stop_data = [
        {'lat': float(stop_latitude),
         'lng': float(stop_longitude)},
        f"{stop_name}",
        int(stop_id),
    ]
    if suburb in data:
        data[suburb].append(stop_data)
    else:
        data[suburb] = [stop_data]

# write data to JSON file
with open('stopList.json', 'w') as json_file:
    json.dump(data, json_file)