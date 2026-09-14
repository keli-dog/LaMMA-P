def prepare_sandwich_ingredients(robots):
    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[1], 'Tomato')
    GoToObject(robots[2], 'Bread')
    GoToObject(robots[3], 'Plate')

    PickupObject(robots[0], 'Lettuce')
    PickupObject(robots[1], 'Tomato')
    PickupObject(robots[2], 'Bread')
    PickupObject(robots[3], 'Plate')

    GoToObject(robots[0], 'CounterTop')
    GoToObject(robots[1], 'CounterTop')
    GoToObject(robots[2], 'CounterTop')
    GoToObject(robots[3], 'Sink')

    PutObject(robots[0], 'Lettuce', 'CounterTop')
    PutObject(robots[1], 'Tomato', 'CounterTop')
    PutObject(robots[2], 'Bread', 'CounterTop')
    PutObject(robots[3], 'Plate', 'Sink')

    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[1], 'Tomato')
    GoToObject(robots[2], 'Bread')
    GoToObject(robots[3], 'Plate')

    SliceObject(robots[0], 'Lettuce')
    SliceObject(robots[1], 'Tomato')
    SliceObject(robots[2], 'Bread')
    CleanObject(robots[3], 'Plate')

def execute_task():
    task_thread1 = threading.Thread(target=prepare_sandwich_ingredients, args=(robots,))
    task_thread1.start()
    task_thread1.join()
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    task_over = True
    time.sleep(5)