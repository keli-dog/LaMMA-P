def wash_fork(robots):
    GoToObject(robots[0], 'Fork')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'SinkBasin')
    PutObject(robots[0], 'Fork', 'SinkBasin')
    SwitchOn(robots[0], 'Faucet')
    CleanObject(robots[0], 'Fork')
    time.sleep(5)
    SwitchOff(robots[0], 'Faucet')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Bowl')
    PutObject(robots[0], 'Fork', 'Bowl')

def turn_off_light(robots):
    GoToObject(robots[0], 'LightSwitch')
    SwitchOff(robots[0], 'LightSwitch')

task1_thread = threading.Thread(target=wash_fork, args=(robots,))
task2_thread = threading.Thread(target=turn_off_light, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)