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
Q1: How long does it take to travel from stop 1 to stop 2 - done
Q2: What is the fastest travel time for that route out of all options 
Q3: What is shortest wait time between each bus for that route at any time in the day
Q4: What is the least amount of bus swaps requried to go from stop 1 to stop 2
Q5: Draw chosen route - done 
'''
# OPTIONAL Q6: Display Bus GPS data on google maps
# Predictive Analytics: predict the next next bus for a given route if the ideal one is missed
# OPTIONAL Predictive Analytics: calculate the probability of a Route being either late Early or on-time using the NXTBUS real-time data API
# Input: XML data of Bus stops, Routes and Position, Output: Bus travel Routes

#import busRequest
import Q2
# import Q3
# import Q4
import Q5
import PredictiveAnalytics
import tkinter
import tkinter.ttk as ttk
import ttkthemes
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from labellines import *
from datetime import datetime
import googlemaps
import csv
import pandas as pd
import os
import webbrowser
from flask import Flask, render_template, url_for


import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("BUS APP")

        #create frames
        self.input_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        self.var = tkinter.StringVar()
        #create label and entry
        self.question_label = tkinter.Label(self.input_frame, text = f"Select Question:")
        option_1 = tkinter.Radiobutton(self.input_frame, text="Question 1", value="Q1", variable= self.var, command=self.show_options)
        option_2 = tkinter.Radiobutton(self.input_frame, text="Question 2", value="Q2", variable= self.var, command=self.show_options)
        option_3 = tkinter.Radiobutton(self.input_frame, text="Question 3", value="Q3", variable= self.var, command=self.show_options)
        option_4 = tkinter.Radiobutton(self.input_frame, text="Question 4", value="Q4", variable= self.var, command=self.show_options)
        option_5 = tkinter.Radiobutton(self.input_frame, text="Question 5", value="Q5", variable= self.var, command=self.show_options)
        option_6 = tkinter.Radiobutton(self.input_frame, text="Question 6", value="Q6", variable= self.var, command=self.show_options)

        #create buttons
        calculate_button = tkinter.Button(self.button_frame, text = "Calculate", command= self.calculate)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)


        #pack labels, entry, buttons and text box
        self.stop_result_label = tkinter.Label(self.result_frame, text=f"")
        self.error_label = tkinter.Label(self.result_frame, text="Please enter a valid route")
        # Pack the radio buttons onto the window
        option_1.pack()
        option_2.pack()
        option_3.pack()
        option_4.pack()
        option_5.pack()
        option_6.pack()
        calculate_button.pack(side='left')
        quit_button.pack(side='left')

        #Q1 and Q4
        self.infoLabel1 = tkinter.Label(self.result_frame, text="Press Calculate and run file in new Python instance")

        #Q3
        self.infoLabel2 = tkinter.Label(self.result_frame, text="Press Calculate to open flask app and webpage to server")

        #Q2 and Q6
        self.stop_1_label = tkinter.Label(self.result_frame, text="Enter Stop 1 number")
        self.stop_1_entry = tkinter.Entry(self.result_frame)
        self.stop_2_label = tkinter.Label(self.result_frame, text="Enter Stop 2 number")
        self.stop_2_entry = tkinter.Entry(self.result_frame)

        #Q5
        self.route_label = tkinter.Label(self.result_frame, text="Enter route number")
        self.route_entry = tkinter.Entry(self.result_frame)
        #pack frames
        self.input_frame.pack(side='left')
        self.button_frame.pack(side='bottom')
        self.result_frame.pack(side='right')
        
        
        #Enter the tkinter main loop
        tkinter.mainloop()

        

    #take user input and display the result
    def calculate(self):
        question = self.var.get()
        if question == "Q5":
            try:
                route = str(self.route_entry.get())
                float(route)
                coords = Q5.data(route)
                if float(route) / 1 == float(route):
                    Q5.main(coords, "red", 2, 50, 4)
            except ValueError:   
                self.error_label.pack()
            else:
                self.error_label.pack_forget()

        elif question == "Q2":
            stop_1 = str(self.stop_1_entry.get())
            stop_2 = str(self.stop_2_entry.get())
            stop_1_name = Q2.stop_name(str(self.stop_1_entry.get()))
            stop_2_name = Q2.stop_name(str(self.stop_2_entry.get()))
            text = Q2.main(stop_1, stop_2, "AIzaSyAzmIkaPnXXghoAImiCqL1wlYW5shytqKE")
            self.stop_result_label.config(text=f"Stop 1: {stop_1_name} \n Stop 2: {stop_2_name} \n Fastest Time: {text}")
            self.stop_result_label.pack()
        elif question == "Q3":
            os.system('app.py')
            webbrowser.open_new_tab('http://127.0.0.1:5000')
        elif question == "Q4":
            # exec(open('Q4.py').read(), None, None)
            os.system('Q4.py')
        elif question == "Q1":
            # exec(open('Q1.py').read(), None, None)
            os.system('Q1.py')
        elif question == "Q6":
            stop_1 = str(self.stop_1_entry.get())
            stop_2 = str(self.stop_2_entry.get())
            PredictiveAnalytics.main(stop_1, stop_2)

    
    def show_options(self):
        self.route_label.pack_forget()
        self.route_entry.pack_forget()
        self.stop_1_label.pack_forget()
        self.stop_1_entry.pack_forget()
        self.stop_2_label.pack_forget()
        self.stop_2_entry.pack_forget()
        self.infoLabel1.pack_forget()
        self.infoLabel2.pack_forget()

        if self.var.get() == "Q5":
            self.route_label.pack()
            self.route_entry.pack()

        elif self.var.get() == "Q1":
            self.infoLabel1.pack()

        elif self.var.get() == "Q2":
            self.stop_1_label.pack()
            self.stop_1_entry.pack()
            self.stop_2_label.pack()
            self.stop_2_entry.pack()

        elif self.var.get() == "Q3":
            self.infoLabel1.pack()
            self.infoLabel2.pack()

        elif self.var.get() == "Q4":
            self.infoLabel1.pack()

        elif self.var.get() == "Q6":
            self.stop_1_label.pack()
            self.stop_1_entry.pack()
            self.stop_2_label.pack()
            self.stop_2_entry.pack()

        
my_gui = myGUI()

key = 'AIzaSyAzmIkaPnXXghoAImiCqL1wlYW5shytqKE'


gmaps = googlemaps.Client(key=key)


xml = busRequest.ptRequest(line=4, direction='B', start='6:00am', end='11:00pm')
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

