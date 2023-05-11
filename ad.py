import tkinter as tk
import turtle
import turtle_square

# create tkinter window and canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# create turtle screen on the canvas
screen = turtle.TurtleScreen(canvas)

# call the turtle square function and display it on the tkinter canvas
turtle_square.draw_square()

# start the tkinter mainloop
root.mainloop()
