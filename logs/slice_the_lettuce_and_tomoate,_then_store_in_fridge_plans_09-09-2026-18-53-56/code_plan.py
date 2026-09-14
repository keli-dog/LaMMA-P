def slice_lettuce(robots):
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Lettuce')
    SliceObject(robots[0], 'Lettuce')
    PutObject(robots[0], 'Knife', 'CounterTop')

def slice_tomato(robots):
    GoToObject(robots[1], 'Knife')
    PickupObject(robots[1], 'Knife')
    GoToObject(robots[1], 'Tomato')
    SliceObject(robots[1], 'Tomato')
    PutObject(robots[1], 'Knife', 'CounterTop')

def store_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Lettuce', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def store_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Tomato', 'Fridge')
    CloseObject(robots[1], 'Fridge')

task1_thread = threading.Thread(target=slice_lettuce, args=(robots,))
task2_thread = threading.Thread(target=slice_tomato, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

task3_thread = threading.Thread(target=store_lettuce, args=(robots,))
task4_thread = threading.Thread(target=store_tomato, args=(robots,))

task3_thread.start()
task4_thread.start()

task3_thread.join()
task4_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)