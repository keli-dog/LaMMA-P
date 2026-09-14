def waste_disposal(robots):
    GoToObject(robots[0], 'GarbageBag')
    PickupObject(robots[0], 'GarbageBag')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'GarbageBag', 'GarbageCan')

def surface_cleaning(robots):
    GoToObject(robots[0], 'CounterTop')
    CleanObject(robots[0], 'CounterTop')
    GoToObject(robots[0], 'DiningTable')
    CleanObject(robots[0], 'DiningTable')

def object_organization(robots):
    GoToObject(robots[1], 'Plate')
    PickupObject(robots[1], 'Plate')
    GoToObject(robots[1], 'Cabinet')
    OpenObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Plate', 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

task1_thread = threading.Thread(target=waste_disposal, args=(robots,))
task2_thread = threading.Thread(target=surface_cleaning, args=(robots,))
task3_thread = threading.Thread(target=object_organization, args=(robots,))

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