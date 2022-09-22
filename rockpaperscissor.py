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

#Write your code below this line 👇
rps = [rock,paper,scissors]
option = int(input("What do you chose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
random_number = random.randint(0,2)
random_variable = rps[random_number]
if option==0:
  print(rps[0])
  print("computer choose")
  print(random_variable)
  if random_number==0:
    print("Draw")
  elif random_number==1:
    print("You lose")
  else:
    print("You win")
elif option==1:
  print(rps[1])
  print("computer choose")
  print(random_variable)
  if random_number==0:
    print("You win")
  elif random_number==1:
    print("Draw")
  else:
    print("You lose")
else:
  print(rps[2])
  print("computer choose")
  print(random_variable)
  if random_number==0:
    print("You lose")
  elif random_number==1:
    print("You win")
  else:
    print("Draw")