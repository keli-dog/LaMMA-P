def process_eggs(robots):
    GoToObject(robots[0], 'Egg')
    PickupObject(robots[0], 'Egg')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Egg', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def process_bread(robots):
    GoToObject(robots[1], 'Bread')
    PickupObject(robots[1], 'Bread')
    GoToObject(robots[1], 'Cabinet')
    OpenObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Bread', 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

def process_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Lettuce', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def process_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Cabinet')
    OpenObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Tomato', 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

task1_thread = threading.Thread(target=process_eggs, args=(robots,))
task2_thread = threading.Thread(target=process_bread, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()

task3_thread = threading.Thread(target=process_lettuce, args=(robots,))
task4_thread = threading.Thread(target=process_tomato, args=(robots,))
task3_thread.start()
task4_thread.start()
task3_thread.join()
task4_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)