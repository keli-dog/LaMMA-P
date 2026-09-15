def prepare_coffee(robots):
    GoToObject(robots[0], 'Mug')
    PickupObject(robots[0], 'Mug')
    GoToObject(robots[0], 'CoffeeMachine')
    SwitchOn(robots[0], 'CoffeeMachine')
    SwitchOff(robots[0], 'CoffeeMachine')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Mug', 'CounterTop')

def setup_mug(robots):
    GoToObject(robots[1], 'Cup')
    PickupObject(robots[1], 'Cup')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Cup', 'CounterTop')

def prepare_tea(robots):
    GoToObject(robots[2], 'Kettle')
    PickupObject(robots[2], 'Kettle')
    GoToObject(robots[2], 'StoveBurner')
    PutObject(robots[2], 'Kettle', 'StoveBurner')
    SwitchOn(robots[2], 'StoveBurner')
    SwitchOff(robots[2], 'StoveBurner')

task1_thread = threading.Thread(target=prepare_coffee, args=(robots,))
task2_thread = threading.Thread(target=setup_mug, args=(robots,))
task3_thread = threading.Thread(target=prepare_tea, args=(robots,))

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