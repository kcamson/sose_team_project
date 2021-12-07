# import everything from the file domain.py
import os

os.system("clear")

# create a dictionary that encapsulates the rules for aquiring points
# key is the expected points, values are a list of dice that would get those points
scenarios = {
    500: [5, 5, 5],
    1000: [1, 1, 1],
    3000: [1, 2, 3, 4, 5, 6],
    400: [4, 4, 4],
    200: [1, 5, 5]
}
# gonna create a bunch of scoring sets from dictionary above
scoring_sets = []

# loop though all the keys
for k in scenarios.keys():

    dice = []
    for i in scenarios[k]:
        pass

    # create a scoring set from dice and append to the list
# once done, loop though all the scoring sets (or the dictionary keys)
# print out the two values and they should match

