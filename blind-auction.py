from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.
print(logo)
auction_dictionary = {}
def highestbid(bidding_record):
  highestbidvalue = 0
  winner =""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highestbidvalue:
      highestbidvalue = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highestbidvalue}")
users = False
while not users:
  name = input("what is your name?: ")
  bid = int(input("How much bid you want to make?: "))
  auction_dictionary[name] = bid
  should_continue = input("there are other users who want to bid?: Type yes or no. ")
  if should_continue=="no":
    users = True
    highestbid(auction_dictionary)
  elif should_continue=="yes":
    clear()
