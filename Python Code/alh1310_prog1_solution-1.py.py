'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Wizard Currency
Collaborators:

Description: This program will convert Wizard currency to Muggle United States currency.
'''


# Input how many knuts, sickles, and galleons you have
knut = float(input ("Enter the number of Knuts you have in your pocket: "))
sickle = float(input ("Enter the number of Sickles you have in your pocket: "))
galleon = float(input ("Enter the number of Galleons you have in your pocket: "))

# Compute the conversions
sickles = sickle * 29
galleons = galleon * 17 * 29
muggle_money = ((knut + sickles + galleons) * 0.1)

# Output the amount of muggle money you have
print("You have a total of $" + "{: .2f}" .format(muggle_money))
