from art import logo
print(logo)

loop= True
bidders={}
while loop:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    bidders[name] = bid
    other_bidders = input("is there anyother bidders, Yes or No: ").lower()

    if other_bidders == "yes":
        print("\n"*20)

    elif other_bidders== "no":
        loop= False

highest = 0
for key in bidders:

    if bidders[key]>highest:
        highest=bidders[key]


for key in bidders:
    if bidders[key]==highest:
        print(f"The winner is {key} with a bid of ${bidders[key]} ")








