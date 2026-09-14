def rotate_tomato(robot):
    GoToObject(robot, 'Tomato')
    PickupObject(robot, 'Tomato')
    GoToObject(robot, 'DiningTable')
    PutObject(robot, 'Tomato', 'DiningTable')
    PickupObject(robot, 'Tomato')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Tomato', 'Fridge')
    PickupObject(robot, 'Tomato')
    CloseObject(robot, 'Fridge')
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Tomato', 'CounterTop')

def rotate_lettuce(robot):
    GoToObject(robot, 'Lettuce')
    PickupObject(robot, 'Lettuce')
    GoToObject(robot, 'DiningTable')
    PutObject(robot, 'Lettuce', 'DiningTable')
    PickupObject(robot, 'Lettuce')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Lettuce', 'Fridge')
    PickupObject(robot, 'Lettuce')
    CloseObject(robot, 'Fridge')
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Lettuce', 'CounterTop')

def rotate_potato(robot):
    GoToObject(robot, 'Potato')
    PickupObject(robot, 'Potato')
    GoToObject(robot, 'DiningTable')
    PutObject(robot, 'Potato', 'DiningTable')
    PickupObject(robot, 'Potato')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Potato', 'Fridge')
    PickupObject(robot, 'Potato')
    CloseObject(robot, 'Fridge')
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Potato', 'CounterTop')

def execute_task(robots):
    task1_thread = threading.Thread(target=rotate_tomato, args=(robots[1],))
    task2_thread = threading.Thread(target=rotate_lettuce, args=(robots[1],))
    task3_thread = threading.Thread(target=rotate_potato, args=(robots[1],))
    
    task1_thread.start()
    task1_thread.join()
    
    task2_thread.start()
    task2_thread.join()
    
    task3_thread.start()
    task3_thread.join()
    
    action_queue.append({'action':'Done'})
    task_over = True
    time.sleep(5)