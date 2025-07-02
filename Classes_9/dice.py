from random import choice
class Dice:
    def __init__(self):
        self.sides=20

    def roll_die(self):
        side = choice(range(1,self.sides+1))
        print(side)



dice_1 = Dice()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()
dice_1.roll_die()