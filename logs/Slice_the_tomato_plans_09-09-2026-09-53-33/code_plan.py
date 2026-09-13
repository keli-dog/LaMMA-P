def slice_tomato(robots):
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[0], 'Tomato')
    SliceObject(robots[0], 'Tomato')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Tomato', 'CounterTop')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Knife', 'CounterTop')

task1_thread = threading.Thread(target=slice_tomato, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)