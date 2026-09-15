def execute_task():
    def robot1_task():
        GoToObject(robots[0], 'Knife')
        PickupObject(robots[0], 'Knife')
        GoToObject(robots[0], 'Lettuce')
        PickupObject(robots[0], 'Lettuce')
        SliceObject(robots[0], 'Lettuce')
        GoToObject(robots[0], 'Cabinet')
        OpenObject(robots[0], 'Cabinet')
        PutObject(robots[0], 'Lettuce', 'Cabinet')
        GoToObject(robots[0], 'Potato')
        PickupObject(robots[0], 'Potato')
        SliceObject(robots[0], 'Potato')
        GoToObject(robots[0], 'Bowl')
        PutObject(robots[0], 'Potato', 'Bowl')
        GoToObject(robots[0], 'CounterTop')
        PutObject(robots[0], 'Knife', 'CounterTop')
        CloseObject(robots[0], 'Bowl')

    def robot2_task():
        GoToObject(robots[1], 'Knife')
        PickupObject(robots[1], 'Knife')
        GoToObject(robots[1], 'Tomato')
        PickupObject(robots[1], 'Tomato')
        SliceObject(robots[1], 'Tomato')
        GoToObject(robots[1], 'Bowl')
        OpenObject(robots[1], 'Bowl')
        PutObject(robots[1], 'Tomato', 'Bowl')
        GoToObject(robots[1], 'CounterTop')
        PutObject(robots[1], 'Knife', 'CounterTop')
        CloseObject(robots[1], 'Cabinet')

    task1_thread = threading.Thread(target=robot1_task)
    task2_thread = threading.Thread(target=robot2_task)

    task1_thread.start()
    task2_thread.start()

    task1_thread.join()
    task2_thread.join()

    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})

    task_over = True
    time.sleep(5)