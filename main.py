# ---------
# @author   Jordan Reed
# @date     12/11/25
# ---------

from math import sqrt
from pneuma_class import Pneuma

my_pneuma = Pneuma()

# fake menu

answer = 10
while(answer != 0):
    my_pneuma.print_pneuma()

    print("\nWhat activity did you do today?")
    print(" (1) Read my bible")
    print(" (2) Pray")
    print("\n (0) Exit Game")

    try:
        answer = int(input("_ "))
    except Exception as e:
        print("You put the wrong character in. Try again.")
        continue

    if answer == 0:
        exit(0)
    elif answer == 1:
        # read bible
        my_pneuma.add_points(75)
    elif answer == 2:
        # pray
        my_pneuma.add_points(150)
    else:
        print("That is an incorrect option. Try again.\n")
    
