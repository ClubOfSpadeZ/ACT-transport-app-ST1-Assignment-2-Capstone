from tkinter import *
import tkinter
import tkinter.ttk as ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from labellines import *
from datetime import datetime, timedelta
import googlemaps
import csv
import pandas as pd

class MyGUI():

    def __init__(self):
        # self.main_window = tkinter.Tk()
        self.canvas = None
        self.main_window = tkinter.Tk()
        self.main_window.geometry("800x650")
        self.main_window.title("Q4")

        self.pickFrame = tkinter.Frame(self.main_window)
        self.pickFrame.pack(side='top')

        self.timenow = datetime.now()
        self.APIkey = 'AIzaSyAzmIkaPnXXghoAImiCqL1wlYW5shytqKE'
        self.client = googlemaps.Client(self.APIkey)

        self.stops = []
        self.selected_stopFrom = tkinter.StringVar(self.pickFrame)
        self.selected_stopTo = tkinter.StringVar(self.pickFrame)

        with open('static/data/stops.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                self.stops.append(row[0])  # Append the stop name to the list

        self.filtered_stopsFrom = self.stops
        self.filtered_stopsTo = self.stops
        print(self.stops)

        self.selected_stopFrom.trace("w", self.filter_stopFrom)
        self.selected_stopTo.trace("w", self.filter_stopTo)

        self.stopFromLabel = ttk.Label(self.pickFrame, text="Stop from")
        self.stopFrom = ttk.Combobox(self.pickFrame, textvariable=self.selected_stopFrom, values=self.filtered_stopsFrom)
        self.stopFromLabel.pack()
        self.stopFrom.pack()

        self.stopToLabel = ttk.Label(self.pickFrame, text="Stop To")
        self.stopTo = ttk.Combobox(self.pickFrame, textvariable=self.selected_stopTo, values=self.filtered_stopsTo)
        self.stopToLabel.pack()
        self.stopTo.pack()

        # Time picker
        self.picktimeFrame = ttk.Frame(self.pickFrame)
        self.picktimeFrame.pack(side='bottom')

        self.midday = ['AM', 'PM']
        self.selected_midday = tkinter.StringVar(self.picktimeFrame)

        self.hour = ttk.Spinbox(self.picktimeFrame, from_=0, to=12, wrap=True, width=3)
        self.colon = ttk.Label(text=':')
        self.minute = ttk.Spinbox(self.picktimeFrame, from_=0, to=59, wrap=True, width=3)
        self.middayOption = ttk.OptionMenu(self.picktimeFrame, self.selected_midday, *self.midday)

        self.hour.pack(side='left', fill='y')
        self.colon.pack(after=self.hour, side='left')
        self.minute.pack(after=self.colon, side='left', fill='y')
        self.middayOption.pack(after=self.minute, side='left', fill=tkinter.BOTH)

        self.swapsLabel = ttk.Label(text='the least amount of bus swaps requried:')
        self.swaps = ttk.Entry(justify='center')

        self.swapsLabel.pack()
        self.swaps.pack()

        def settimenow():
            self.hour.delete(0, 'end')
            self.hour.insert(0, str(self.timenow.strftime("%I")))

            self.minute.delete(0, 'end')
            self.minute.insert(0, str(self.timenow.minute))

            if self.timenow.strftime('%p') == "AM":
                self.selected_midday.set(self.midday[0])
            else:
                self.selected_midday.set(self.midday[1])

        self.submit = ttk.Button(self.main_window, text="submit", command=self.getRoute)
        self.submit.pack(pady=10)

        self.quit = ttk.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.quit.pack(pady=10, after=self.submit)

        self.filter_stopFrom()
        self.filter_stopTo()

        settimenow()

        tkinter.mainloop()

    def filter_stopFrom(self, *args):
        typed = self.selected_stopFrom.get()
        self.filtered_stopsFrom = [stop for stop in self.stops if typed.lower() in stop.lower()]
        self.stopFrom["values"] = self.filtered_stopsFrom

    def filter_stopTo(self, *args):
        typed = self.selected_stopTo.get()
        self.filtered_stopsTo = [stop for stop in self.stops if typed.lower() in stop.lower()]
        self.stopTo["values"] = self.filtered_stopsTo

    def Graph(self, time, routes, stops):
        def nested_list(start, stop):
            result = []
            for i in range(start, stop):
                result.append([i, i + 1])
            return result

        y = nested_list(0, 5)

        # Convert time data to datetime objects
        time = [[datetime.strptime(t, '%I:%M%p') for t in sublist] for sublist in time]

        # Create plot
        fig = Figure(figsize=(15, 5), dpi=100)
        fig.subplots_adjust(bottom=0.2)
        ax = fig.add_subplot(111)

        i = 0

        for index1, sublist in enumerate(time):
            for index2, t in enumerate(sublist):
                ax.plot(time[index1][index2], y[index1][index2], marker='o', color='navy')
                # Add label to current point
                ax.text(time[index1][index2], y[index1][index2], stops[index1][index2], ha='center', va='bottom', rotation=45, fontsize=8)
                if index2 > 0:
                    # Draw a line between the current point and the previous point
                    ax.plot([time[index1][index2 - 1], time[index1][index2]],
                            [y[index1][index2 - 1], y[index1][index2]], color='navy', label=routes[i])
                    i += 1
                elif index1 > 0:
                    start = time[index1 - 1][1]
                    end = time[index1][0]
                    ax.plot([start, end], [y[index1 - 1][1], y[index1][0]], linestyle='--', color='gray',
                            label='Waiting')

        ax.set_xlabel('Time')
        ax.set_ylabel('Distance')
        ax.set_title('Bus Schedule')
        ax.legend()

        # Set x-axis format
        date_fmt = '%I:%M%p'
        date_formatter = matplotlib.dates.DateFormatter(date_fmt)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xticks([t for sublist in time for t in sublist])

        # Rotate x-axis labels by 45 degrees
        for label in ax.get_xticklabels():
            label.set_rotation(45)

        # Remove old canvas if it exists
        for widget in self.main_window.winfo_children():
            if isinstance(widget, tkinter.Canvas):
                widget.pack_forget()

        # Create new canvas
        canvas = FigureCanvasTkAgg(fig, master=self.main_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)


    def getRoute(self):
        self.swaps.delete(0, END)

        hour = self.hour.get()
        minute = self.minute.get()
        midday = self.selected_midday.get()


        time_str = f'{hour}:{minute}{midday}'
        time = datetime.combine(self.timenow, datetime.strptime(time_str, '%I:%M%p').time())
        print(f"{time}\n{self.stopFrom.get()}\n{self.stopTo.get()}")



        def getcoords(stop_id):
            coords = {}
            df = pd.read_csv('static/data/stops.csv')

            stop_lat, stop_lon = df.loc[df['stop_id'] == int(stop_id), ['stop_lat', 'stop_lon']].iloc[0]
            coords["lat"] = stop_lat
            coords["lng"] = stop_lon
            return coords

        def getdirections(origin, destination, time):
            directions_result = self.client.directions(origin, destination, mode='transit', departure_time=time, transit_routing_preference='fewer_transfers')
            return directions_result

        data = getdirections(getcoords(self.stopFrom.get()), getcoords(self.stopTo.get()), time)

        Route = []
        on_bus = []
        off_bus = []
        on_stop = []
        off_stop = []

        for leg in data[0]["legs"]:
            for step in leg["steps"]:
                if step["travel_mode"] == "TRANSIT":
                    Route.append(step['transit_details']['line']['short_name'])
                    on_bus.append(step['transit_details']['departure_time']['text'].replace('\u202f', ''))
                    off_bus.append(step['transit_details']['arrival_time']['text'].replace('\u202f', ''))
                    on_stop.append(step['transit_details']['departure_stop']['name'])
                    off_stop.append(step['transit_details']['arrival_stop']['name'])

        data = {
            'Route': Route,
            'On bus': on_bus,
            'Off Bus': off_bus,
            'On stop': on_stop,
            'Off stop': off_stop,
        }

        df = pd.DataFrame(data)

        num_rows = df.shape[0]
        self.swaps.insert(0, str(num_rows))
        print(num_rows)

        # set max_rows and max_columns to None
        pd.set_option('display.max_rows', 1000)
        pd.set_option('display.max_columns', 10)

        time = df[['On bus', 'Off Bus']].values.tolist()
        routes = df['Route'].values.tolist()
        stops = df[['On stop', 'Off stop']].values.tolist()

        # Load the stops.csv file into a DataFrame
        stops_df = pd.read_csv('static/data/stops.csv')

        # Create a dictionary mapping stop_name values to stop_id values
        stops_dict = dict(zip(stops_df['stop_name'], stops_df['stop_id']))

        # Convert stop_name values to stop_id values in list1
        stops = [[stops_dict[stop_name] if stop_name in stops_dict else stop_name for stop_name in sublist] for sublist in stops]

        print(time)
        print(routes)
        print(stops)
        self.Graph(time, routes, stops)


MyGUI()