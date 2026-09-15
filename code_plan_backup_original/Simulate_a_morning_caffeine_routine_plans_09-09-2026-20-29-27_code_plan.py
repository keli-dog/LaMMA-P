def coffee_preparation(robots):
    GoToObject(robots[0], 'CoffeeMachine')
    GoToObject(robots[0], 'Mug')
    PickupObject(robots[0], 'Mug')
    PutObject(robots[0], 'Mug', 'CoffeeMachine')
    SwitchOn(robots[0], 'CoffeeMachine')
    time.sleep(300)
    SwitchOff(robots[0], 'CoffeeMachine')

def tea_preparation(robots):
    GoToObject(robots[1], 'Kettle')
    GoToObject(robots[1], 'Cup')
    PickupObject(robots[1], 'Kettle')
    PutObject(robots[1], 'Kettle', 'SinkBasin')
    SwitchOn(robots[1], 'Faucet')
    time.sleep(5)
    SwitchOff(robots[1], 'Faucet')
    PickupObject(robots[1], 'Kettle')
    PutObject(robots[1], 'Kettle', 'StoveBurner')
    SwitchOn(robots[1], 'StoveBurner')
    PickupObject(robots[1], 'Cup')
    PutObject(robots[1], 'Cup', 'CounterTop')
    time.sleep(420)
    PickupObject(robots[1], 'Kettle')
    PutObject(robots[1], 'Kettle', 'CounterTop')
    SwitchOff(robots[1], 'StoveBurner')

def cleanup(robots):
    CleanObject(robots[0], 'Mug')
    CleanObject(robots[1], 'Cup')

task1_thread = threading.Thread(target=coffee_preparation, args=(robots,))
task2_thread = threading.Thread(target=tea_preparation, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

task3_thread = threading.Thread(target=cleanup, args=(robots,))
task3_thread.start()
task3_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)