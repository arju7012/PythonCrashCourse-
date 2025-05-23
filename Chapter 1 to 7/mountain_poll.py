#creating an empty dictionary to store the responses.
responses = {}

#creating a flag to check the poll is still active of not.
poll_active = True

while poll_active:
    name = input("What's your name: ")
    place = input("Where would you like to climb a mountain ?")
    responses[name] = place

    check = input("If anyone else want to poll? (yes of no)")
    if check == 'no':
        poll_active = False

for name, place in responses.items():
    print(f"{name.title()} like to go to {place}")