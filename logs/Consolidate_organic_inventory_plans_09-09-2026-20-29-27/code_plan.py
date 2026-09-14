def consolidate_apple(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Apple', 'CounterTop')

def consolidate_lettuce(robots):
    GoToObject(robots[1], 'Lettuce')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Lettuce', 'CounterTop')

def consolidate_tomato(robots):
    GoToObject(robots[0], 'Tomato')
    PickupObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Tomato', 'CounterTop')

def consolidate_potato(robots):
    GoToObject(robots[1], 'Potato')
    PickupObject(robots[1], 'Potato')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Potato', 'CounterTop')

def consolidate_bread(robots):
    GoToObject(robots[1], 'Bread')
    PickupObject(robots[1], 'Bread')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Bread', 'CounterTop')

def consolidate_egg(robots):
    GoToObject(robots[1], 'Egg')
    PickupObject(robots[1], 'Egg')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Egg', 'CounterTop')

task1_thread = threading.Thread(target=consolidate_apple, args=(robots,))
task2_thread = threading.Thread(target=consolidate_lettuce, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

task3_thread = threading.Thread(target=consolidate_tomato, args=(robots,))
task4_thread = threading.Thread(target=consolidate_potato, args=(robots,))

task3_thread.start()
task4_thread.start()

task3_thread.join()
task4_thread.join()

task5_thread = threading.Thread(target=consolidate_bread, args=(robots,))
task5_thread.start()
task5_thread.join()

task6_thread = threading.Thread(target=consolidate_egg, args=(robots,))
task6_thread.start()
task6_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)