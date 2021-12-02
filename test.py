# import everything from the file domain.py
import models.poll
from models.player import User
from models.poll import Poll

import os
os.system("clear")


# this is how you create objects from a class file
player = Player("jonathan", 23)
player2 = Player("sebastian", 4)
player3 = Player("chi chi", 12)

# create a game and pass in a list of players
game = Game([player, player2, player3])

print(game)
print(f"first player is {game.current_player()}")
for i in range(5):
    game.next_player()
    print(game.current_player().first_name)

# die = StandardDie()
# print(die.current_value())
# die2 = StandardDie(5)
# print(die2.current_value())
#
# for i in range(10):
#     # loop 10 times, and print the result of the dice.roll() method
#     die.roll()
#     print(die.current_value())
