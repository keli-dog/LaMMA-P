def wash_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Sink')
    CleanObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Lettuce', 'CounterTop')

def place_tomato(robots):
    GoToObject(robots[0], 'Tomato')
    PickupObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Tomato', 'CounterTop')

task1_thread = threading.Thread(target=wash_lettuce, args=(robots,))
task2_thread = threading.Thread(target=place_tomato, args=(robots,))
task1_thread.start()
task1_thread.join()
task2_thread.start()
task2_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)