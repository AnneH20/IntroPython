'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment:
Collaborators:

Description: Create a program that will run the 2 functions from
             the Activity 8 Module
'''

# Import Ascii art functions from module
import alh1310_activity8_module


def main():
    # Call to Ascii Diamond function
    alh1310_activity8_module.ascii_diamond(5, '*')
    alh1310_activity8_module.ascii_diamond(4, '#')
    alh1310_activity8_module.ascii_diamond(3, '$')

    # Call to Ascii Christmas Tree function
    alh1310_activity8_module.ascii_christmas_tree(9)
    alh1310_activity8_module.ascii_christmas_tree(7)
    alh1310_activity8_module.ascii_christmas_tree(5)

main()