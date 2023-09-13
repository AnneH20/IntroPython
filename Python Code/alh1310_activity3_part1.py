'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: 
Collaborators:

Description: Questions 1-3 allows the user to input their height and favorite color. Question 4 is a program that calculates the amount due.
'''

# Question 1: Input user's height
height = float(input("Enter your height (Round round to the nearest foot): "))

# Question 2: Input user's favorite color
color = input("Enter your favorite color: ")

# Question 3: Output My name is <my netid>! My height is <height> and my favorite color is <favortie color>
print("My name is Alh1310! My height is: ", height, "and my favorite color is: ", color)


# Question 4:
# Assign the sum of 9999 and 4563 to the variable total
total = (9999 + 4563)

# Assign the value 3500 to the variable down_payment
down_payment = 3500

# Subract the value in down_payment from the value in total and assign the difference to the variable due
due = total - down_payment

# Output the value in due preceded by the messsage "You must pay"
print("You must pay: ", due)

