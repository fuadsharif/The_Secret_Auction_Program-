from art import logo
print(logo)

def find_highest_bidder(bidder_record):
    highest=0
    winner=""
    for key in bidder_record:
        if bidder_record[key]>highest:
            highest = bidder_record[key]
            winner = key
    print(f"The winner is {winner} with the bid of ${highest}")







bidders={}
loop= True
while loop:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    bidders[name] = bid
    other_bidders = input("is there anyother bidders, Yes or No: ").lower()

    if other_bidders == "yes":
            print("\n"*100)

    elif other_bidders== "no":
        loop= False
        find_highest_bidder(bidders)