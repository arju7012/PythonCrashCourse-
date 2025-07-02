import random

probabilities = [1,2,3,4,5,6,7,8,9,10,'a', 'b', 'c', 'd', 'e', ]

winning_ticket = random.sample(probabilities,4)

print(f"\nThe final winning ticket is : {winning_ticket}")