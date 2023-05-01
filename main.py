# Author: Rory Birnie u3261233, Akhil u3261101
# Date created: 13 Apr 2023
# Date last changed: 13 Apr 2020
# This program will be the main interfaces for all other script used for making a transport App for ACT buses
# the databases to be used are as follows,
# Bus Stops XML data from https://data.gov.au/dataset/ds-act-https%3A%2F%2Fwww.data.act.gov.au%2Fapi%2Fviews%2F7vpw-vmgx/details?q=action%20bus
# Bus Routes XML data from https://data.gov.au/dataset/ds-act-https%3A%2F%2Fwww.data.act.gov.au%2Fapi%2Fviews%2Fifm8-78yv/details?q=action%20bus
# OPTIONAL NXTBUS real-time data API https://data.gov.au/dataset/ds-act-https%3A%2F%2Fwww.data.act.gov.au%2Fapi%2Fviews%2Fsmqx-37iq/details?q=action%20bus
# to display the data we will used the google maps python libray and graphs to show travel and wait times
'''
Q1: How long does it take to travel from stop 1 to stop 2
Q2: What is the fastest travel time for that route out of all options
Q3: What is shortest wait time between each bus for that route at any time in the day
Q4: What is the least amount of bus swaps requried to go from stop 1 to stop 2
Q5: Draw chosen route - done 
'''
# OPTIONAL Q6: Display Bus GPS data on google maps
# Predictive Analytics: predict the next next bus for a given route if the ideal one is missed
# OPTIONAL Predictive Analytics: calculate the probability of a Route being either late Early or on-time using the NXTBUS real-time data API
# Input: XML data of Bus stops, Routes and Position, Output: Bus travel Routes

import busRequest
import xml.etree.ElementTree as et
import pandas
import googlemaps

key = 'AIzaSyAzmIkaPnXXghoAImiCqL1wlYW5shytqKE'

gmaps = googlemaps.Client(key=key)


xml = busRequest.ptRequest(line=4, direction='B', start='12:30pm', end='12:40pm')
# print(xml)

# parse the XML data
tree = et.ElementTree(et.fromstring(xml.decode()))
root = tree.getroot()

# print(et.tostring(root, encoding='unicode', method='xml'))
# create an empty list to store the data
data = []

# loop through each DatedCall element and extract the required information
for dated_call in root.findall('.//{http://www.siri.org.uk/siri}DatedCall'):
    stop_point_ref = dated_call.find('{http://www.siri.org.uk/siri}StopPointRef').text
    stop_point_name = dated_call.find('{http://www.siri.org.uk/siri}StopPointName').text
    try:
        aimed_arrival_time = dated_call.find('{http://www.siri.org.uk/siri}AimedArrivalTime').text
    except AttributeError:
        aimed_arrival_time = None
    try:
        aimed_departure_time = dated_call.find('{http://www.siri.org.uk/siri}AimedDepartureTime').text
    except AttributeError:
        aimed_arrival_time = None
    data.append([stop_point_ref, stop_point_name, aimed_arrival_time, aimed_departure_time])

# create a Pandas DataFrame with the data and column names
df = pandas.DataFrame(data, columns=['StopPointRef', 'StopPointName', 'AimedArrivalTime', 'AimedDepartureTime'])

print(df.to_string(index=True))
