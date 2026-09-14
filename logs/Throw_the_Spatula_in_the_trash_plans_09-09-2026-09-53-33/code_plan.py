def throw_spatula(robots):
    GoToObject(robots[0], 'Spatula')
    PickupObject(robots[0], 'Spatula')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'Spatula', 'GarbageCan')

def execute_task():
    throw_spatula([robot0])