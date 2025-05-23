prompt = "Tell me your age: "

active = True
while active:
    age = input(prompt)
    if age == "quit":
        active = False   
    elif int(age) < 3:
        print("The ticket is free!!")
    elif 3 < int(age) < 12:
        print("Ticket is $10")
    elif int(age) >= 12:
        print("Ticket is $15.")
    