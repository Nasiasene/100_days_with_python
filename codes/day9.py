dict = {}
retry = True
def auction(name, bid):
    dict[name] = bid
    return dict
def biggest_bid(dict):
    counter = 0
    for key in dict:
        if dict[key] > counter:
            counter = dict[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${counter}.")


print("\nWelcome to the secret auction program.")
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction(name, bid)
    retry = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if retry == "no":
        break
    elif retry == "yes":
        continue
    else:
        while retry != "yes" and retry != "no":
            retry = input("Please type 'yes' or 'no'.\n").lower()
            if retry == "yes" or retry == "no":
                break

biggest_bid(dict)