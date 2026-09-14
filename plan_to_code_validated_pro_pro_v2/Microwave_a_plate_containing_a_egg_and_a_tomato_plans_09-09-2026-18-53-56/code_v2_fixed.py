def prepare_plate(robots):
    GoToObject(robots[1], 'Plate')
    if not robots[1].GetHandObject():
        PickupObject(robots[1], 'Plate')

def prepare_egg(robots):
    GoToObject(robots[1], 'Egg')
    PickupObject(robots[1], 'Egg')
    GoToObject(robots[1], 'Plate')
    if robots[1].GetHandObject() and robots[1].GetHandObject().objectId == 'Plate':
        PutObject(robots[1], 'Egg', 'Plate')

def prepare_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Plate')
    if robots[1].GetHandObject() and robots[1].GetHandObject().objectId == 'Plate':
        PutObject(robots[1], 'Tomato', 'Plate')

def place_in_microwave(robots):
    GoToObject(robots[1], 'Microwave')
    OpenObject(robots[1], 'Microwave')
    time.sleep(1)
    PutObject(robots[1], 'Plate', 'Microwave')
    CloseObject(robots[1], 'Microwave')

def microwave_food(robots):
    GoToObject(robots[1], 'Microwave')
    SwitchOn(robots[1], 'Microwave')
    time.sleep(1)
    time.sleep(30)
    SwitchOff(robots[1], 'Microwave')

task1_thread = threading.Thread(target=prepare_plate, args=(robots,))
task2_thread = threading.Thread(target=prepare_egg, args=(robots,))
task3_thread = threading.Thread(target=prepare_tomato, args=(robots,))
task4_thread = threading.Thread(target=place_in_microwave, args=(robots,))
task5_thread = threading.Thread(target=microwave_food, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()
task1_thread.join()
task2_thread.join()
task3_thread.join()
task4_thread.start()
task4_thread.join()
task5_thread.start()
task5_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)