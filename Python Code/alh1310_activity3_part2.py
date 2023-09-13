# Title: Activity 3 Part 2
# Author: Anne Marie Heidebreicht

# Description: This program calculates the volume of a cone

# Input because you are assigning a number to the variable pi, a number to the variable r, and a number to the variable h
pi = 3.14
r = float(input("Enter the radius of your cone: "))
h = float(input("Enter the height of your cone: "))

# Process because you are plugging in the data from the variables into the equation for volume
volume = pi * (r ** 2) * (h / 3)

# Output because you are showing the result of the volume equation
print("The volume is ", volume)
