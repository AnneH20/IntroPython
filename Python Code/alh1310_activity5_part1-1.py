'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: 
Collaborators:

Description: Write a program that generates 3 passwords based on a user's input and output the results
'''

# Question 1
color = input("What is your favorite color? ")

# Question 2
number = (input("What is your favorite number? "))

# Question 3
pet = input("What is the name of your pet? ")

# Question 4
password1 = (number + pet + color)

# Question 5
password2 = (color + number + pet)

# Question 6
password3 = (pet + number + color)

# Question 7
print("Password 1 is: ", password1)
print("Password 2 is: ", password2)
print("Password 3 is: ", password3)

