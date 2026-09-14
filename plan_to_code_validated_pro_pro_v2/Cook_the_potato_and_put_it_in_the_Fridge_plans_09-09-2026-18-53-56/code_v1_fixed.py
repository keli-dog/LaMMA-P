def cook_potato(robots):
    # Robot 0 handles potato and knife
    GoToObject(robots[0], 'Potato')
    PickupObject(robots[0], 'Potato')
    GoToObject(robots[0], 'Pan')
    PutObject(robots[0], 'Potato', 'Pan')
    
    # Robot 1 handles pan and stove
    GoToObject(robots[1], 'Pan')
    PickupObject(robots[1], 'Pan')
    GoToObject(robots[1], 'StoveBurner')
    PutObject(robots[1], 'Pan', 'StoveBurner')
    GoToObject(robots[1], 'StoveKnob')
    SwitchOn(robots[1], 'StoveKnob')
    time.sleep(10)  # Cooking time
    
    # Robot 0 picks up cooked potato
    GoToObject(robots[0], 'Pan')
    PickupObject(robots[0], 'Potato')
    
    # Robot 1 turns off stove
    GoToObject(robots[1], 'StoveKnob')
    SwitchOff(robots[1], 'StoveKnob')
    
    # Robot 0 slices potato
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    SliceObject(robots[0], 'Potato')
    PutObject(robots[0], 'Knife', 'CounterTop')
    
    # Robot 0 puts potato in fridge
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Potato', 'Fridge')
    CloseObject(robots[0], 'Fridge')

task1_thread = threading.Thread(target=cook_potato, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)