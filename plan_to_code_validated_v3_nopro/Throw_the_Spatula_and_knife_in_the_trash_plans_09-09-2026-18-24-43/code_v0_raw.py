def throw_objects(robots):
    GoToObject(robots[0], 'Spatula')
    GoToObject(robots[1], 'Knife')
    PickupObject(robots[0], 'Spatula')
    PickupObject(robots[1], 'Knife')
    GoToObject(robots[0], 'GarbageCan')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[0], 'Spatula', 'GarbageCan')
    PutObject(robots[1], 'Knife', 'GarbageCan')

task1_thread = threading.Thread(target=throw_objects, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)