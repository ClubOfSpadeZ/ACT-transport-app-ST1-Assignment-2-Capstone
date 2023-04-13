ACT transport app for ST1-Assignment 2 Capstone at University of Canberra

Author: Rory Birnie u3261233, Akhil u3261101
Date created: 13 Apr 2023

This program will be the main interfaces for all other script used for making a transport App for ACT buses
the databases to be used are as follows,

Bus Stops XML data from 
https://data.gov.au/dataset/ds-act-https%3A%2F%2Fwww.data.act.gov.au%2Fapi%2Fviews%2F7vpw-vmgx/details?q=action%20bus
Bus Routes XML data from
https://data.gov.au/dataset/ds-act-https%3A%2F%2Fwww.data.act.gov.au%2Fapi%2Fviews%2Fifm8-78yv/details?q=action%20bus
OPTIONAL NXTBUS real-time data API 
https://data.gov.au/dataset/ds-act-https%3A%2F%2Fwww.data.act.gov.au%2Fapi%2Fviews%2Fsmqx-37iq/details?q=action%20bus

to display the data we will used the google maps python libray and graphs to show travel and wait times
Q1: Make an program that displays the travel and wait time between two locations using a time / distance graph (from Lanyon Marketplace to Taylor Adventure Playground)
Q2: Display the fastest travel time for Route of Q1
Q3: Display the shortest amount of wait time of Route in Q1
Q4: Display the least amount of Route change overs
Q5: Display the safest route using the Sunday timetable (a safe route will have multiple options to get to a location if a bus is missed or missing)
OPTIONAL Q6: Display Bus GPS data on google maps from the NXTBUS API

Predictive Analytics: predict the next next bus for a given route if the ideal one is missed
OPTIONAL Predictive Analytics: calculate the probability of a Route being either late Early or on-time using the NXTBUS real-time data API

Input: XML data of Bus stops, Routes and Position, Output: Bus travel Routes on maps and graphs.
