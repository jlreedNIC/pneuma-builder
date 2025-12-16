# --------
# @file     activity_class.py
# @author   Jordan Reed
# @date     12/11/25
# @brief    the activity class. defines what activities give points
# ---------

# -----
# TO DO:
#  - [ ]  want to only give reward if completed first time in repeat occurance
#    - ex: if reading bible multiple times per day, don't give points

import datetime as dt

class Activity:
    def __init__(self, desc="NA", reward=0, last_comp=None, repeat="daily"):
        """ date of form MM/DD/YYYY """
        self.name = desc
        self.pneuma_reward = reward
        self.repeat_occurance = repeat
        self.date_last_completed = dt.datetime.now()

        if type(last_comp) is str:
            try:
                self.date_last_completed = dt.datetime.strptime(last_comp, "%m/%d/%Y")
            except:
                print('date bug message')
        elif type(last_comp) is dt.datetime:
            self.date_last_completed = last_comp
            
    
    def complete_activity(self):
        """
        Mark activity as completed today. Return the reward amount in order for adding to point total

        :return: point reward amount
        """
        self.date_last_completed = dt.datetime.now()
        return self.pneuma_reward

    def print_activity(self):
        print(f'\nActivity: {self.name}')
        print(f'Reward: {self.pneuma_reward}')
        print(f'Occurance: {self.repeat_occurance}')
        print(f'Date last completed: {self.date_last_completed.strftime("%m/%d/%Y")}')
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __eq__(self, other):
        return (self.name == other.name) and (self.pneuma_reward == other.pneuma_reward) and (self.repeat_occurance == other.repeat_occurance) and (self.date_last_completed == other.date_last_completed)

if __name__ == "__main__":
    print("Testing activity class")

    act = Activity(last_comp="something")
    act.print_activity()

    act = Activity(last_comp="01/05/2024")
    act.print_activity()

    act1 = Activity(desc="Reading bible", reward=75, last_comp=dt.datetime(2024, 9, 12))
    act.print_activity()

    pts = act.complete_activity()
    act.print_activity()
    print(f'Points received: {pts}')

    # comparison
    print(f'comparing {act1 > act}')

    # equals comparison
    print(f'eq compare {act1 == act}')