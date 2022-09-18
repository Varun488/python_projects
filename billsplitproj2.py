print("Welcome to tip calculator")
amount = float(input("What was the total bill? $"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
op1 = 12
op2 = 15
op3 = 10
percenctage = int(input(f"What percentage tip would you like to give {op3}, {op1} or {op2}?"))
split = int(input("How many people want to split bill?"))
new_per = 1 + (percenctage/100)
ans = float(amount/split) * new_per
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("each person should pay: {:0.2f}" .format(ans))