# ---------
# @author   Jordan Reed
# @date     12/11/25
# ---------

from math import sqrt
from pneuma_class import Pneuma
from activity_class import Activity

my_pneuma = Pneuma()
act_bible = Activity("Read bible", 50, "01/01/2024")
act_pray = Activity("Pray", 100, "01/01/2024")

# fake menu

answer = 10
while(answer != 0):
    my_pneuma.print_pneuma()

    print("\nWhat activity did you do today?")
    print(f" (1) {act_bible.name}")
    print(f" (2) {act_pray.name}")
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
        my_pneuma.add_points(act_bible.complete_activity())
        act_bible.print_activity()
    elif answer == 2:
        # pray
        my_pneuma.add_points(act_pray.complete_activity())
        act_pray.print_activity()
    else:
        print("That is an incorrect option. Try again.\n")
    
