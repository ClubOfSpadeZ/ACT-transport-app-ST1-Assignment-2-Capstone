import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Pound to Kilogram Calculator")

        #create frames
        self.input_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.Weight_label = tkinter.Label(self.input_frame, text = "Mass in Pounds: ")
        self.Weight_entry = tkinter.Entry(self.input_frame)
        
        #create buttons
        calculate_button = tkinter.Button(self.button_frame, text = "Calculate", command= self.calculate)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame)

        #pack labels, entry, buttons and text box
        self.Weight_label.pack(side='left')
        self.Weight_entry.pack(side='left')
        calculate_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.input_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def calculate(self):
        result_string = ""

        #clears the text box every time new entrys are displayed
        self.results_tb.delete('1.0', tkinter.END)
        
        weight = float(self.Weight_entry.get())
        weight = weight*0.454
        result_string = f"Weight = {weight} kg"
        self.results_tb.insert('1.0', result_string)

my_gui = myGUI()