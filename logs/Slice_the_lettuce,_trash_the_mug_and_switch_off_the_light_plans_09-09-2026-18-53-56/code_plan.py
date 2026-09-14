def slice_lettuce(robots):
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Lettuce')
    SliceObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Knife', 'CounterTop')

def trash_mug(robots):
    GoToObject(robots[1], 'Mug')
    PickupObject(robots[1], 'Mug')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Mug', 'GarbageCan')

def switch_off_light(robots):
    GoToObject(robots[2], 'LightSwitch')
    SwitchOff(robots[2], 'LightSwitch')

task1_thread = threading.Thread(target=slice_lettuce, args=(robots,))
task2_thread = threading.Thread(target=trash_mug, args=(robots,))
task3_thread = threading.Thread(target=switch_off_light, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)