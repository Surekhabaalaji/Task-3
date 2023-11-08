import random

options=["rock","paper","scissors"]
running=True

while running:
    player=None
    computer=random.choice(options)
    
    while player not in options:
        player=input("Enter your choice(rock,paper,scissors):")
        
    print(f"player:{player}")
    print(f"computer:{computer}")
    
    if player==computer:
        print("Tie!")
    
    elif player=="rock" and computer=="scissors":
         print("You Win!")
   
    elif player=="paper" and computer=="rock":
        print("You Win!")
    
    elif player=="scissors" and computer=="paper":
        print("You Win!")
    
    else:
         print("You Lose")
   
    
    if not input("Play again?(YES/NO)").upper()=="YES":
            running=False
    
print("Hope you enjoy it!")