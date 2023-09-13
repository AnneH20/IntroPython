'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Activity 7
Collaborators:

Description: This program suggests tip amounts based on the cost of a meal
at a restaurant.
'''

# Ask user for the cost of their meal.
meal_cost = float(input("Enter the meal cost: "))


# Calculate the tip percentage amounts based on the user's meal cost.
eighteen_percent = meal_cost * 0.18
twenty_percent = meal_cost * 0.20
twenty_five_percent = meal_cost * 0.25


# Output the tip percentage amounts.
print("18% tip: ", eighteen_percent)
print("20% tip: ", twenty_percent)
print("25% tip: ", twenty_five_percent)
