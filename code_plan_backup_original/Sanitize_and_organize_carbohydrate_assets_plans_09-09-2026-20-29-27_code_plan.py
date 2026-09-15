def store_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Lettuce', 'Fridge')

def store_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Tomato', 'Fridge')

def clean_bread(robots):
    GoToObject(robots[0], 'Bread')
    PickupObject(robots[0], 'Bread')
    GoToObject(robots[0], 'Sink')
    PutObject(robots[0], 'Bread', 'Sink')
    SwitchOn(robots[0], 'Faucet')
    time.sleep(5)
    SwitchOff(robots[0], 'Faucet')
    PickupObject(robots[0], 'Bread')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Bread', 'CounterTop')

def store_bread(robots):
    GoToObject(robots[0], 'Bread')
    PickupObject(robots[0], 'Bread')
    GoToObject(robots[0], 'Cabinet')
    PutObject(robots[0], 'Bread', 'Cabinet')
    CloseObject(robots[0], 'Cabinet')

def handle_potato(robots):
    GoToObject(robots[1], 'Potato')
    PickupObject(robots[1], 'Potato')
    GoToObject(robots[1], 'Sink')
    PutObject(robots[1], 'Potato', 'Sink')
    SwitchOn(robots[1], 'Faucet')
    time.sleep(5)
    SwitchOff(robots[1], 'Faucet')
    PickupObject(robots[1], 'Potato')
    GoToObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Potato', 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

def handle_apple(robots):
    GoToObject(robots[2], 'Apple')
    PickupObject(robots[2], 'Apple')
    GoToObject(robots[2], 'Sink')
    PutObject(robots[2], 'Apple', 'Sink')
    SwitchOn(robots[2], 'Faucet')
    time.sleep(5)
    SwitchOff(robots[2], 'Faucet')
    PickupObject(robots[2], 'Apple')
    GoToObject(robots[2], 'Fridge')
    PutObject(robots[2], 'Apple', 'Fridge')
    CloseObject(robots[2], 'Fridge')

task1_thread = threading.Thread(target=store_lettuce, args=(robots,))
task2_thread = threading.Thread(target=store_tomato, args=(robots,))
task3_thread = threading.Thread(target=clean_bread, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()

task4_thread = threading.Thread(target=store_bread, args=(robots,))
task5_thread = threading.Thread(target=handle_potato, args=(robots,))
task6_thread = threading.Thread(target=handle_apple, args=(robots,))

task4_thread.start()
task5_thread.start()
task6_thread.start()

task4_thread.join()
task5_thread.join()
task6_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)