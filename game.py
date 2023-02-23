import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Rules:
# Rock wins against scissors.
# Paper wins against rock
# Scissors win against paper.

#Write your code below this line 👇

options_to_choose = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for 'rock', 1 for 'paper' or 2 for 'scissors'? "))

if player_choice >= 3 or player_choice < 0:
  print("You entered invalid number.")  
else:  
  print(options_to_choose[player_choice])
  
  computer_choice = random.randint(0,2)
  print(f" Computer choose:\n {options_to_choose[computer_choice]}")

  if player_choice != computer_choice:  
    if player_choice == 0 and computer_choice == 2 :
      print("You won")
    elif player_choice == 1 and computer_choice == 0:
      print("You won")
    elif player_choice == 2 and computer_choice == 1:
      print("You Won.")
    else:
      print("You lost")  
  else:
    print("The game is a Draw.")