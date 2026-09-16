def throw_spatula(robots):
    GoToObject(robots[0], 'Spatula')
    PickupObject(robots[0], 'Spatula')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'Spatula', 'GarbageCan')

def throw_knife(robots):
    GoToObject(robots[1], 'Knife')
    PickupObject(robots[1], 'Knife')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Knife', 'GarbageCan')

task1_thread = threading.Thread(target=throw_spatula, args=(robots,))
task2_thread = threading.Thread(target=throw_knife, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)