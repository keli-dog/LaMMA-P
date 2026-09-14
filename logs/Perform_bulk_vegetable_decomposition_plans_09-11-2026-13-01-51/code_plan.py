def slice_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    SliceObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Bowl')
    PutObject(robots[0], 'Lettuce', 'Bowl')

def slice_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    SliceObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Bowl')
    PutObject(robots[1], 'Tomato', 'Bowl')

def slice_potato(robots):
    GoToObject(robots[2], 'Potato')
    SliceObject(robots[2], 'Potato')
    PickupObject(robots[2], 'Potato')
    GoToObject(robots[2], 'Bowl')
    PutObject(robots[2], 'Potato', 'Bowl')

task1_thread = threading.Thread(target=slice_lettuce, args=(robots,))
task2_thread = threading.Thread(target=slice_tomato, args=(robots,))
task3_thread = threading.Thread(target=slice_potato, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)