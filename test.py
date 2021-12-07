# import everything from the file domain.py
import models.poll
from models.poll import Poll

import os
os.system("clear")

# create a game and pass in a list of players
poll = Poll()

print(poll.pollId)


# die = StandardDie()
# print(die.current_value())
# die2 = StandardDie(5)
# print(die2.current_value())
#
# for i in range(10):
#     # loop 10 times, and print the result of the dice.roll() method
#     die.roll()
#     print(die.current_value())
