def wash_fork_put_in_bowl(robots):
    GoToObject(robots[0], 'Fork')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Sink')
    CleanObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Bowl')
    PutObject(robots[0], 'Fork', 'Bowl')

def turn_off_light(robots):
    GoToObject(robots[1], 'LightSwitch')
    SwitchOff(robots[1], 'LightSwitch')

task1_thread = threading.Thread(target=wash_fork_put_in_bowl, args=(robots,))
task2_thread = threading.Thread(target=turn_off_light, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)