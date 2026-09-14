def slice_potato_clean_plate(robots):
    GoToObject(robots[0], 'Knife')
    GoToObject(robots[1], 'Plate')
    PickupObject(robots[0], 'Knife')
    PickupObject(robots[1], 'Plate')
    GoToObject(robots[0], 'Potato')
    GoToObject(robots[1], 'Sink')
    SliceObject(robots[0], 'Potato')
    CleanObject(robots[1], 'Plate')
    GoToObject(robots[0], 'Potato')
    PickupObject(robots[0], 'Potato')
    GoToObject(robots[0], 'Plate')
    PutObject(robots[0], 'Potato', 'Plate')

def execute_task():
    task_thread1 = threading.Thread(target=slice_potato_clean_plate, args=(robots,))
    task_thread1.start()
    task_thread1.join()
    action_queue.append({'action':'Done'})
    task_over = True
    time.sleep(5)