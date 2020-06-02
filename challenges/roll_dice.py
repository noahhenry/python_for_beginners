import random


class Dice:
  def roll(self):
    generate_number = random.randint(1, 6)
    dice1 = generate_number
    dice2 = generate_number

    return (dice1, dice2) # note: parenthesis are not needed as python will automatially interpret this as a tuple


dice_set = Dice()
print(dice_set.roll())