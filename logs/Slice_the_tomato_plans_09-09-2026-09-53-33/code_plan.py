def slice_tomato(robots):
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Tomato')
    PickupObject(robots[0], 'Tomato')
    SliceObject(robots[0], 'Tomato')
    PutObject(robots[0], 'Tomato', 'CounterTop')
    PutObject(robots[0], 'Knife', 'CounterTop')

task_thread = threading.Thread(target=slice_tomato, args=(robots,))
task_thread.start()
task_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)