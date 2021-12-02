# import everything from the file domain.py
from models.dice import *
from models.roll import Roll
from models.scoring_set import ScoringSet

import os
os.system("clear")
dice = []

die1 = StandardDie(5)
die2 = StandardDie(5)
die3 = StandardDie(5)
die4 = StandardDie(5)

dice = [die1, die2, die3, die4]
print("initial values")
for d in dice:
    print(d.current_value())

roll = Roll(dice)
roll.roll()

print("values after rolling")
for d in dice:
    print(d.current_value())
print(ScoringSet(dice).points())

roll.roll()

print("values after second roll")
for d in dice:
    print(d.current_value())

print(ScoringSet(dice).points())
