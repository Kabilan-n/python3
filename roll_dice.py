import random
class Dice:
    def roll(self):
        numb1=random.randint(1,6)
        numb2=random.randint(1,6)
        return numb1,numb2
dice=Dice()
a=dice.roll()
print(a)

