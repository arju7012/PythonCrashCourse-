sandwich_orders = ['pastrami', 'club', 'reuben','tuna salad','pastrami', 'chicken salad', 'philly cheesesteak', 'italian sub', 'pastrami']
finished_sandwiches = []

print("Deli is run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()} Sandwich")
    finished_sandwiches.append(sandwich)

print("\n")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} Sandwich")
