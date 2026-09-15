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

task1_thread = threading.Thread(target=store_lettuce, args=(robots,))
task2_thread = threading.Thread(target=store_tomato, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True