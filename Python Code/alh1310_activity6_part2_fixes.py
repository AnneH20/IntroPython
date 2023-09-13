'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Activity 6 Part 2
Collaborators:

Description: Debug a program
'''

print("Let's Improve your Password!\n\n")

# Ask the user for their current password
current_password = input("Enter your current password: ")

# Create a new string that will store the new password
new_password = ""

# Loop for every character in the current password
for char in current_password:

    # Use if statements to replace certain characters
    # with other characters, and if the character is not
    # in our list, add the original character to the new
    # password.
    if char == "i":
        new_password += "!"
    elif char == "a":
        new_password += "*"
    elif char == "m":
        new_password += "M"
    elif char == "B":
        new_password += "8"
    elif char == "o":
        new_password += "."
    else:
        new_password += char

print("Here are some changes I made to your current password: ", new_password)
