'''
Program Author: Anne Marie Heidebreicht
MSU NetID: alh1310
Assignment: Program 3: Repetition with BlackJack
Collaborators:

Description: This program will allow a single user to play a simplified version of blackjack.
'''
import random


player_score = random.randint(2, 13) + random.randint(2, 13)
house_facecard = random.randint(2, 13)
house_score = random.randint(2, 13) + house_facecard

print("Player score: ", player_score, "House face up card: ", house_facecard)

if player_score > 22 and house_score < 22:
    print("House wins.")
    
else:
    question = input("Continue (y or n): ")

    if question == 'y' and player_score < 22:
        while player_score < 22:
            player_score = player_score + random.randint(2, 13)
            house_score = house_score + random.randint(2, 13)
            print("Player score: ", player_score, "House face up card: ", house_facecard)
            if player_score < 22:
                question = input("Continue (y or n): ")
                if question == 'y':
                    continue
                if question == 'n':
                    print("Player score: ", player_score, "House score: ", house_score)
                    if house_score > 22 and player_score < 22:
                        print("Player wins.")
                    elif player_score > house_score and player_score < 22:
                        print("Player wins.")
                    else:
                        print("House wins.")
                break
            elif player_score > 22:
                print("Player score: ", player_score, "House score: ", house_score)
                print("House wins.")
                break
            
    elif question == 'n':
        print("Player score: ", player_score, "House score: ", house_score)
        if house_score > 22 and player_score < 22:
            print("Player wins.")
        elif player_score > house_score and player_score < 22:
            print("Player wins.")
        else:
            print("House wins.")



