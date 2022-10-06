import random
from replit import clear


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.




def sum(list):
  sum =0
  for i in list:
    sum += i
  return sum
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def calculate_score(list):
  if 11 in list and 10 in list and len(list)==2:
    return 0
  if 11 in list and sum(list)>21:
    list.remove(11)
    list.append(1)
  return sum(list)
def compare(userscore,computerscore):
  if userscore==0:
    return "You Win"
  elif computerscore==0:
    return "You Lose"
  elif userscore>21:
    return "You Lose"
  elif computerscore>21:
    return "You Win"
  elif userscore==computerscore:
    return "Draw"
  else:
    if userscore> computerscore:
      return "You Win"
    else:
      return "You Lose"
def playgame():
  user_cards = []
  computer_cards = []
  isgameover = False
  for _ in range(0,2):
    choice1 = deal_card()
    user_cards.append(choice1)
    choice2 = deal_card()
    computer_cards.append(choice2)
  
    
  while not isgameover:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your cards: {user_cards} and your score is: {user_score}")
    print(f"computer's first card is: {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      isgameover = True
    else:
      draw_card = input("you want to draw another card yes or no: ")
      if draw_card == "yes":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        
      if draw_card =="no":
        isgameover = True
  
  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card());
    computer_score = calculate_score(computer_cards)
  print(f" Your final cards are {user_cards}, your score is {user_score}")
  print(f"computer's final cards are {computer_cards}, computer's score is {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play game of BlackJack? Type Y or N: ")=="Y":
  clear()
  playgame()
