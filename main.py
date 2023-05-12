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
#import xml.etree.ElementTree as et
#import pandas
#import googlemaps
# import Q1
# import Q2
# import Q3
# import Q4
import Q5
import tkinter


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
        self.error_label = tkinter.Label(self.result_frame, text="Please enter a valid route")
        self.question_label.pack()
        # Pack the radio buttons onto the window
        option_1.pack()
        option_2.pack()
        option_3.pack()
        option_4.pack()
        option_5.pack()
        option_6.pack()
        calculate_button.pack(side='left')
        quit_button.pack(side='left')


        #pack frames
        self.input_frame.pack(side='left')
        self.button_frame.pack(side='bottom')
        self.result_frame.pack(side='right')
        
        
        #Enter the tkinter main loop
        tkinter.mainloop()

        

    #take user input and display the result
    def calculate(self):
        question = self.var.get()
        self.error_label.pack_forget()
        if question == "Q5":
            try:
                route = str(self.route_entry.get())
                float(route)
                coords = Q5.data(route)
                if float(route) / 1 == float(route):
                    Q5.main(coords, "red", 2, 50, 4)
            except ValueError:   
                self.error_label.pack()
      
        # elif question == "Q2":
        #     Q2.main()
        # # elif question == "Q3":
        # #     Q3.main()
        # # elif question == "Q4":
        # #     Q4.main()
        # elif question == "Q1":
            #Q1.main()
        # elif question == "Q6":
            #Q6.main()
        ...

    
    def show_options(self):
        if self.var.get() == "Q5":
            self.route_label = tkinter.Label(self.result_frame, text="Enter route number")            
            self.route_entry = tkinter.Entry(self.result_frame)
            self.route_label.pack()
            self.route_entry.pack()
        else:
            self.route_label.pack_forget()
            self.route_entry.pack_forget()
        
        
my_gui = myGUI()
#Q5.main(coords, "red", 2, 50, 4)

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

