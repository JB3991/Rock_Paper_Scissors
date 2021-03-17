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

rps_images = [rock, paper, scissors]

users_choice = int(input("Rock, Paper or Scissors? 0 for rock, 1 for paper and 2 for scissors \n"))

if users_choice >= 3 or users_choice < 0:
  print("You typed an invalid number. YOU LOSE!")
else:
  print(rps_images[users_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(rps_images[computer_choice])


  if users_choice == 0 and computer_choice == 2:
    print("You Win")
  elif computer_choice == 0 and users_choice == 2:
    print("You LOSE")
  elif computer_choice > users_choice:
    print("You LOSE")
  elif users_choice > computer_choice:
    print("You WIN")
  elif users_choice == computer_choice:
    print("You DRAW")
  else: 
    print("You typed an invalid number. YOU LOSE!")