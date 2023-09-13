'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Program 2: Right Triangles with If Statements
Collaborators:

Description: Write a program that asks the user for the sides of a triangle and determines if the 3 sides make a right triangle.
'''

# Ask user to input the length of sides a, b, and c.
a_side = int(input("Enter the length of side a: "))
b_side = int(input("Enter the length of side b: "))
c_side = int(input("Enter the length of side c: "))

# Calculate if the sides make a right triangle and output the correct statements.
if a_side**2 + b_side**2 == c_side**2:
    print("The sides entered for a, b, and c do form a right triangle. The hypotenuse is: ", c_side)
elif c_side**2 + a_side**2 == b_side**2:
    print("The sides entered for a, b, and c do form a right triangle. The hypotenuse is: ", b_side)
elif b_side**2 + c_side**2 == a_side**2:
    print("The sides entered for a, b, and c do form a right triangle. The hypotenuse is: ", a_side)
elif a_side**2 + b_side**2 != c_side**2:
    print("The sides entered for a, b, and c do not form a right triangle.")
elif c_side**2 + b_side**2 != a_side**2:
    print("The sides entered for a, b, and c do not form a right triangle.")
elif c_side**2 + a_side**2 != b_side**2:
    print("The sides entered for a, b, and c do not form a right triangle.")
