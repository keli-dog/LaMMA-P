def wash_fork(robots):
    GoToObject(robots[0], 'Fork')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'SinkBasin')
    PutObject(robots[0], 'Fork', 'SinkBasin')
    SwitchOn(robots[0], 'Faucet')
    CleanObject(robots[0], 'Fork')
    SwitchOff(robots[0], 'Faucet')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Bowl')
    PutObject(robots[0], 'Fork', 'Bowl')

task1_thread = threading.Thread(target=wash_fork, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True