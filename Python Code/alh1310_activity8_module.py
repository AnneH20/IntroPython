'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Activity 8
Collaborators:

Description: Create 2 functions that make ascii art.
'''



# Create function that makes a Christmas tree
# Make parameters size and symbol
def ascii_christmas_tree(size):
    x = size - 1
    y = 1
    for count in range(size):
        print(' ' * x + '^' * y + ' ' * x)
        y += 2
        x -= 1      # Tried to make a trunk, but couldn't figure out how to
                    # center with the tree so I left it out



# Create function that makes a diamond shape
# Make parameters length and symbol
def ascii_diamond(length, symbol):
    # Top of the diamond
    x = 0
    for i in range(1, length + 1):
        for n in range(1, (length - i) + 1):
            print(end=" ")

        while x != (2 * i - 1):
            print(symbol, end="")
            x = x + 1
        x = 0
        print()


    # Bottom of the diamond
    y = 1
    z = 1
    for i in range(1, length):
        for n in range(1, y + 1):
            print(end=" ")
        y = y + 1

        while z <= (2 * (length - i) - 1):
            print(symbol, end="")
            z = z + 1
        z = 1
        print()
