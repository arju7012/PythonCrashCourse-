prompt = "Enter series of pizza toppings (Enter 'quit' to quit): "

flag = True
while flag:
    topping = input(prompt)
    if topping != "quit":
        print(f"You added {topping} on the pizza!!")
    else:
        flag = False