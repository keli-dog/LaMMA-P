def throw_spatula(robots):
    GoToObject(robots[0], 'Spatula')
    PickupObject(robots[0], 'Spatula')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'Spatula', 'GarbageCan')

task1_thread = threading.Thread(target=throw_spatula, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)