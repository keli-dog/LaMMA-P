def store_eggs(robots):
    GoToObject(robots[0], 'Egg')
    PickupObject(robots[0], 'Egg')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Egg', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def clean_plate(robots):
    GoToObject(robots[1], 'Plate')
    PickupObject(robots[1], 'Plate')
    CleanObject(robots[1], 'Plate')
    GoToObject(robots[1], 'Cabinet')
    OpenObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Plate', 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

def close_cabinets(robots):
    GoToObject(robots[1], 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

def turn_off_appliances(robots):
    GoToObject(robots[0], 'CoffeeMachine')
    SwitchOff(robots[0], 'CoffeeMachine')
    GoToObject(robots[0], 'Microwave')
    SwitchOff(robots[0], 'Microwave')

def clean_cup(robots):
    GoToObject(robots[1], 'Cup')
    PickupObject(robots[1], 'Cup')
    CleanObject(robots[1], 'Cup')
    GoToObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Cup', 'Cabinet')

def turn_off_lights(robots):
    GoToObject(robots[0], 'LightSwitch')
    SwitchOff(robots[0], 'LightSwitch')

task1_thread = threading.Thread(target=store_eggs, args=(robots,))
task2_thread = threading.Thread(target=clean_plate, args=(robots,))
task3_thread = threading.Thread(target=close_cabinets, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()

task4_thread = threading.Thread(target=turn_off_appliances, args=(robots,))
task5_thread = threading.Thread(target=clean_cup, args=(robots,))

task4_thread.start()
task5_thread.start()

task4_thread.join()
task5_thread.join()

turn_off_lights(robots)

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)