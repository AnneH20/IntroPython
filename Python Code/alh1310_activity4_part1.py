'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Activity 4 Part 1
Collaborators:

Description: Write a program that will output your GPA numerical grade if you input your letter grade.
'''

# Question 1
letter_grade = str(input("Enter your letter grade on the A-F scale (Type in capital letters only): "))

# Question 2

if letter_grade == 'A':
    gpa = 4.0
elif letter_grade == 'B':
    gpa = 3.0
elif letter_grade == 'C':
    gpa = 2.0
elif letter_grade == 'D':
    gpa = 1.0
elif letter_grade == 'F':
    gpa = 0.0
else:
    gpa = -1.0

# Question 3
print("Your GPA is: ", gpa)
