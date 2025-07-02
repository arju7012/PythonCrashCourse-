import random

probabilities = [1,2,3,4,5,6,7,8,9,10,'a', 'b', 'c', 'd', 'e', ]

my_ticket = random.sample(probabilities,4)

attempt = 0

while True:
    attempt += 1
    drawn_ticket = random.sample(probabilities,4)
    if set(drawn_ticket) == set(my_ticket):
        break

    

print(f"Your ticket : {my_ticket}")
print(f"It tooks {attempt} tries to get a winning match.")