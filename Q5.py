import turtle
import csv

def data(route):
    with open('static\data\Bus_Routes.csv', 'r') as file:

        # Create a CSV reader object
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        coords = ""
        # Iterate over each row in the CSV file
        for row in reader:
            if row[4] == route:
                coords = row[0]

        return coords

def remove_extras(coords : str):
    '''
    Removes the MULTILINESTRING ((...)) part and separates each entry by commas
    '''
    coords = coords.replace("MULTILINESTRING ((","").replace("))", "")
    coordinates_str = coords
    # split into multiple pairs
    coordinates_list = coordinates_str.split(", ")
    return coordinates_list

#convert the first values into float
def convert_to_int(coordinates_list : list):
    '''
    Converts list to float for getting accurate coordinates
    '''
    AX, AY = map(float, coordinates_list[0].split())
    AX = int(AX)
    AY = int(AY)

    return AX, AY

def get_raw_coordinates(coordinates_list : list):
    '''
    converts coordinates from API to a lsit (does not make it usuable for drawing the map)
    '''
    raw_coordinates = []
    for pair in coordinates_list:
        x, y = pair.split(" ")
        raw_coordinates.append((x, y))
    
    return raw_coordinates

def set_screen():
    '''
    Create main screen 
    '''
    wl = -1000
    wb = -1000
    wr = 1000
    wt = 1000
    turtle.Screen().setworldcoordinates(wl, wb, wr, wt)

def get_coordinates(raw_coordinates : list, coordinates_list: list, multiplier:int):
    '''
    Converts raw coordinates to usuable coordinates by removing the whole number value from the float and using a multiplier
    '''
    coordinates = []
    trun_x = trun(coordinates_list)[0]
    trun_y = trun(coordinates_list)[1]
    MULTIPLIER = multiplier*1000
    X0 = ((float(raw_coordinates[0][0]) - trun_x) *MULTIPLIER)
    Y0 = (((float(raw_coordinates[0][1])+ abs(trun_y))*MULTIPLIER))
    

    for i in range(len(raw_coordinates)):
        x = ((float(raw_coordinates[i][0]) - trun_x) *MULTIPLIER) - X0
        y = (((float(raw_coordinates[i][1])+ abs(trun_y))*MULTIPLIER)) - Y0

        coordinates.append((float(x), float(y)))
    return coordinates

def draw_route(coordinates , colour, size):
    '''
    Draws the route using the coordinates from get_coordinate function
    '''
    turtle.color(colour)
    turtle.pensize(size)
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(0,0)
    turtlepos = []
    for i in range(0, len(coordinates)):
        turtle.goto(coordinates[i])
        turtle.pendown()
        turtlepos.append(turtle.position())
        turtle.hideturtle()

    return turtlepos

def rescale_image(map_pos: list, border : int):
    '''
    Scales the map to fit the screen in case it goes off screen or is too big
    '''
    wl = min(map_pos, key=lambda x: x[0])
    wr = max(map_pos, key=lambda x: x[0])
    wb = min(map_pos, key=lambda x: x[1])
    wt = max(map_pos, key=lambda x: x[1])

    WHITESPACE = border
    turtle.Screen().setworldcoordinates(wl[0]-WHITESPACE, wb[1]-WHITESPACE, wr[0]+WHITESPACE, wt[1]+WHITESPACE)

def trun(coordinates_list : list):
    '''
    Separates the int value from the floats
    '''
    trun_x = float(convert_to_int(coordinates_list)[0])
    trun_y = float(convert_to_int(coordinates_list)[1])

    return list((trun_x, trun_y))

def main(coords, colour, size, border, multiplier):
    '''
    Uses functions to draw the map,
    coords = coordinates can use API to get them,
    colour = map line color,
    size = pen size for map drawing,
    border = border around the map to keep away from corners of the screen,
    multiplier = the size map is drawn at
    '''
    set_screen()
    # split each pair into x and y components
    coordinates_list = remove_extras(coords)
    raw_coordinates = list(get_raw_coordinates(coordinates_list))
    coordinates = list(get_coordinates(raw_coordinates, coordinates_list, multiplier))
    map_pos = draw_route(coordinates, colour, size)
    rescale_image(map_pos, border)
    turtle.mainloop()
