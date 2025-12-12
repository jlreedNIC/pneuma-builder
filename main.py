# ---------
# @author   Jordan Reed
# @date     12/11/25
# ---------

from math import sqrt

def update_pneuma_level(points):
    level = (-5 + sqrt(25+2*points))/10

    return int(level) + 1
    """
    0 - 99 : level 1 : 100 pts
    100 - 299 : level 2 : 200 pts
    300 - 500 : level 3 : 300 pts

    level = 
    """

def print_status(points, level):
    print(f'Status')
    print(f'------')
    print(f'pneuma points: {points}')
    print(f'pneuma level: {level}')

pneuma_points = 0
pneuma_level = 1

print(update_pneuma_level(pneuma_points))

# fake menu

answer = 10
while(answer != 0):
    print_status(pneuma_points, pneuma_level)

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
        pneuma_points += 75
    elif answer == 2:
        # pray
        pneuma_points += 150
    else:
        print("That is an incorrect option. Try again.\n")
    
    # update
    pneuma_level = update_pneuma_level(pneuma_points)
