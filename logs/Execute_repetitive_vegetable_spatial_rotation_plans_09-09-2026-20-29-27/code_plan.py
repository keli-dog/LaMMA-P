def rotate_vegetables(robots):
    GoToObject(robots[1], 'DiningTable')
    GoToObject(robots[1], 'Fridge')
    
    GoToObject(robots[1], 'CounterTop')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'DiningTable')
    PutObject(robots[1], 'Lettuce', 'DiningTable')
    
    GoToObject(robots[1], 'DiningTable')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Tomato', 'Fridge')
    CloseObject(robots[1], 'Fridge')
    
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PickupObject(robots[1], 'Potato')
    CloseObject(robots[1], 'Fridge')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Potato', 'CounterTop')
    
    GoToObject(robots[1], 'DiningTable')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Lettuce', 'Fridge')
    CloseObject(robots[1], 'Fridge')
    
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PickupObject(robots[1], 'Tomato')
    CloseObject(robots[1], 'Fridge')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Tomato', 'CounterTop')
    
    GoToObject(robots[1], 'CounterTop')
    PickupObject(robots[1], 'Potato')
    GoToObject(robots[1], 'DiningTable')
    PutObject(robots[1], 'Potato', 'DiningTable')
    
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PickupObject(robots[1], 'Lettuce')
    CloseObject(robots[1], 'Fridge')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Lettuce', 'CounterTop')
    
    GoToObject(robots[1], 'CounterTop')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'DiningTable')
    PutObject(robots[1], 'Tomato', 'DiningTable')
    
    GoToObject(robots[1], 'DiningTable')
    PickupObject(robots[1], 'Potato')
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Potato', 'Fridge')
    CloseObject(robots[1], 'Fridge')

task_thread = threading.Thread(target=rotate_vegetables, args=(robots,))
task_thread.start()
task_thread.join()

action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)