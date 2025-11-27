from logo import logos
from data import data
import random

vs_logos = [
    """
 __     __ 
 \ \   / / 
  \ \ / /  
   \ V /   
    \_/    
"""
]

score = 0
choosedlogo = random.choice(logos)
print(choosedlogo)

while True:
    choiceone = random.choice(data)
    choicetwo = random.choice(data)

    while choiceone == choicetwo:
        choicetwo = random.choice(data)


    print(f"Option A: {choiceone["name"]} is {choiceone["description"]} from {choiceone["country"]}")
    print(vs_logos[0])
    print(f"Option B: {choicetwo["name"]} is {choicetwo["description"]} from {choicetwo["country"]}")

    userchoice = input("Which option you think has More Followers: (A or B): ").lower()

    if  choiceone["followers"] > choicetwo["followers"]:
        if userchoice == "a":
            print("You Wins")
            score += 1
        else:
            print("You Loose")
            break
    else:
        if userchoice == "b":
            print("you wins")
            score += 1
        else:
            print("You loose!")
            break

print(score)

