import tkinter as tk

def hide_text():
    text.pack_forget()

def show_text():
    text.pack()

# Create a window and a button
window = tk.Tk()
button_hide = tk.Button(window, text="Hide Text", command=hide_text)
button_show = tk.Button(window, text="Show Text", command=show_text)

# Create a text widget
text = tk.Label(window, text="This is some text.")

# Pack the widgets onto the window
text.pack()
button_hide.pack()
button_show.pack()

# Run the window
window.mainloop()
