import turtle

def draw_square():
    t = turtle.Turtle()
    for i in range(4):
        t.forward(100)
        t.right(90)

if __name__ == '__main__':
    draw_square()
    turtle.mainloop()
