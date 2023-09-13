'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Activity 4 Part 2
Collaborators:

Description: Indicating sets of values of x for each if/else-if/else statements that you make each statement to output as true.
'''


x = int(input("Enter a number: "))

# Statement 1: x = [11, 19]
if x > 10 and x < 20:
    print("if Statement 1 Executed!")
      
# Statement 2: x = [21, ∞)
if x < 10 and x > 20:
    print("if Statement 2 Executed!")

# Statement 3: x = [ 11, ∞) or (-∞, 19]
if x > 10 or x < 20:
    print("if Statement 3 Executed!")
      
# Statement 4: x = (-∞, 9] or [21, ∞)
if x < 10 or x > 20:
    print("if Statement 4 Executed!")
      
# Statement 5: x = 2 or x = 3
if x == 2 or x == 3:
    print("if Statement 5 Executed!")
      
# Statement 6: x = (-∞, 1] [4, ∞)
if x != 2 and x != 3:
    print("if Statement 6 Executed!")
      
# Statement 7: (-∞, 1] or [4, ∞)
if x != 2 or x != 3:
    print("if Statement 7 Executed!")
