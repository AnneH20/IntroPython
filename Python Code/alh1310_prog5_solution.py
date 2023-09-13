"""
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Program 5: Functions with Turtle Graphics
Collaborators:

Description: Write a program that produces a colorful graphic.
"""

# Import turtle library
import turtle
# Import random library
import random


def trim_in_bounds(value):
    """
         Step 4:  The parameter value should be a float. Regardless
         of the value of the parameter value, you want to return a value
         between 0 and 1.
     """

    if value < 0:
        return 0
    elif value > 1:
        return 1
    return value


def random_offset(color):
    # Unpack RGB values from color
    r, g, b = color
    # Select one of the three values
    clr = random.randint(0, 2)
    # Randomly create an offset
    offset = (random.random() - 0.5) / 5
    if clr == 0:
        # Add random selected color to offset
        update_color = r + offset
        # Set the color equal to the function call trim_in_bounds
        # with the randomly selected color as the argument
        r = trim_in_bounds(update_color)
    elif clr == 1:
        update_color = g + offset
        g = trim_in_bounds(update_color)
    elif clr == 2:
        update_color = b + offset
        b = trim_in_bounds(update_color)
    # Return new color
    return r, g, b

    """
        Step 3: Delete pass. The parameter color should be a tuple. You can access
        or unpack the RGB values from color using the following r, g, b = color.
        RGB should be float values between 0 and 1 representing how much red, green,
        and blue are in the color.
        
        Once you have your r, g, b values, you need to select one of the 3 values.
        Next you need to randomly create an offset. This random offset should be
        between -0.1 and 0.1.  The larger the range the more drastically the colors
        will change.  The smaller the range, the more subtle the color changes
        will be.  Feel free to play with this range.
        This line of code will generate a random value between -0.1 and 0.1.
        (random.random()- 0.5)/5
        
        Now that you have randomly selected a color and generated a random offset
        between -0.1 and 0.1, you need to add the offset to the randomly selected
        color.  After you add the offset to the randomly selected color, set the
        color equal to the function call trimInBounds with the randomly selected
         color as the argument.
         
        Lastly return r, g, b
    """


def draw_line(x1, y2):
    # Pick pen up
    t.up()
    # Go to coordinates (x1, 0)
    t.goto(x1, 0)
    # Set pen down
    t.down()
    # Go to coordinates (0, y2)
    t.goto(0, y2)
    # Pick pen up
    t.up()
    # Set pen color
    r, g, b = random_offset(t.color()[0])
    t.color((r, g, b))
    """ 
        (x1, y2) is the coordinate for where the cursor currently is. 
        To understand how this function works you need the imagine a box where one 
        corner is determined by the point (0,0) and the opposite corner is wherever 
        the cursor is being dragged too. 
        This function draws a line by 
            -picking the turtle's pen up 
            -telling the turtle to goto the point (x1, 0) which is on corner above 
                (0,0) and opposite the point (x1, y2) 
            -putting the pen back down 
            -telling the turtle to goto the point (0, y2) which is the point below 
                (x1, y2) and opposite the point (0,0) 
            -then pick the pen back up which is not necessary, but I think is a 
                good habit 
        .                              .(x1, y2) 
            . 
                  . 
                       . 
                            . 
                                 . 
                                     . 
        .(0,0) 

        Step 1: Figure out how to draw the lines. Look into the following methods  
        t.up(), t.down(), and t.goto(). To run the program, click run and the  
        drag the circle in the middle of the turtle window around. 

        Step 2:  Add the following two lines of code to this function. 
                r, g, b = random_offset1(t.color()[0]) 
                t.color((r, g, b)) 
    """


# t is a python turtle
t = turtle.Turtle()
t.up()
t.shape("circle")
t.color((random.random(), random.random(), random.random()))
wn = turtle.Screen()
wn.listen()
wn.tracer(0)
t.ondrag(draw_line)
wn.mainloop()
