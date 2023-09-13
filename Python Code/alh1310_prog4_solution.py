'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Program 4: Analyzing Text Files using String Functions
Collaborators:

Description: This program will analyze a text document and use string analysis to
determine how many letters, numbers, punctuation marks, and words are in the text
'''


# Ask the user for the name of their text file
file_name = input("Enter the full name of your file.\nExample: file_name.txt\n---->:  ")

# Open the file in read mode and store the text
# in the variable called file_text
with open(file_name,"r") as file_obj:
    file_text = file_obj.read()

# file_text will contain the text you will have
# to analyze for this program.
num_digits = 0
num_punc = 0
num_letters = 0

# Create a list that stores all punctuation symbols.
punc_list = ['.', '?', '!', ',', ';', ':', '-', '–', '—', '(', ')', '[', ']', '{', '}', "'", '"', '…']


# Code that counts everything.
for char in file_text:
# Find number of letters.
    if (char.isalpha()) == True:
        num_letters += 1
# Find number of digits.
    elif (char.isdigit()) == True:
        num_digits += 1
# Find number of punctuation marks.
    elif char in punc_list:
        num_punc += 1

# Find word count.
word_count = 0
# I did google how to separate file text by whitespace:
# https://www.w3schools.com/python/ref_string_split.asp
separate_text = file_text.split()
for element in separate_text:
    count = 0
    for char in element:
        if (char.isalpha()) == True:
            count += 1
    if count > 0:
        word_count += 1




# Output the results
print("Number of Letters: ", num_letters)
print("Number of Digits: ", num_digits)
print("Number of Punctuation Marks: ", num_punc)
print("Number of valid words: ", word_count)