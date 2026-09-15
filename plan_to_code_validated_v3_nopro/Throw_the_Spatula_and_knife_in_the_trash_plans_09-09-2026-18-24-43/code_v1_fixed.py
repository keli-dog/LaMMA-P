def throw_objects(robots):
    GoToObject(robots[0], 'Spatula')
    PickupObject(robots[0], 'Spatula')
    GoToObject(robots[0], 'GarbageCan')
    ThrowObject(robots[0], 'Spatula', 'GarbageCan')
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'GarbageCan')
    ThrowObject(robots[0], 'Knife', 'GarbageCan')

throw_objects(robots)
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)