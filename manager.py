# --------
# @file     manager.py
# @author   Jordan Reed
# @date     12/15/25
# @brief    the main controller of the pneuma builder. Handles the pneuma class and activity list
# ---------

from pneuma_class import Pneuma
from activity_class import Activity
import datetime as dt

class Game_Manager:
    def __init__(self):
        self.my_pneuma = Pneuma()
        self.current_activities = []
        self.date_last_updated = dt.datetime.now()
    
    def add_activity(self, activity=None):
        """
        Activity is either of type Activity Class or a list of up to length 4 where:
        [0]: activity name
        [1]: reward amount
        [2]: date completed
        [3]: repeat occurance

        :param activity: _description_, defaults to None
        """
        if type(activity) == Activity:
            self.current_activities.append(activity)
        elif type(activity) == list:
            name = activity[0]
            reward = 0
            completed = None
            repeat = "daily"
            if len(activity) >= 2:
                reward = activity[1] 
            if len(activity) >= 3:
                completed = activity[2]
            if len(activity) >= 4:
                repeat = activity[3]

            act = Activity(name, reward, completed, repeat)
            self.current_activities.append(act)
        else:
            print("incorrect activity passed")
    
    def remove_activity(self, activity):
        if type(activity) == Activity:
            self.current_activities.remove(activity)
        else:
            print("this isn't implemented yet")
    
    def print_activity_list(self):
        print(f"\nActivity List")
        print(f'-------------')
        for act in self.current_activities:
            act.print_activity()

if __name__ == "__main__":
    gm = Game_Manager()

    # add activity
    gm.add_activity(Activity())
    gm.print_activity_list()

    # add activity by list
    gm.add_activity(['act name'])
    gm.print_activity_list()

    # add activity by list
    gm.add_activity(['act name1', 50])
    gm.print_activity_list()

    # add activity by list
    gm.add_activity(['act name2', 50, "12/01/2025"])
    gm.print_activity_list()

    # add activity by list
    gm.add_activity(['act name3', 50, "12/01/2025", "weekly"])
    gm.print_activity_list()

    # remove activity
    gm.remove_activity(Activity())
    gm.print_activity_list()

