vacation = {}

poll_active = True

while poll_active:
    name = input("What is your name: ")
    place = input("If you could visit one place in the world, where would you go? : ")

    vacation[name] = place

    check = input("If there is anyone else to take poll? (yes or no)")
    if check == "no":
        poll_active = False

for name, place in vacation.items():
    print(f"{name.title()} like to visit {place.title()}")