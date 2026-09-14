def execute_task(robots):
    def robot1_task(robots):
        GoToObject(robots[0], 'Apple')
        PickupObject(robots[0], 'Apple')
        GoToObject(robots[0], 'Fridge')
        OpenObject(robots[0], 'Fridge')
        PutObject(robots[0], 'Apple', 'Fridge')
        CloseObject(robots[0], 'Fridge')

    def robot2_task(robots):
        GoToObject(robots[1], 'LightSwitch')
        SwitchOff(robots[1], 'LightSwitch')

    task1_thread = threading.Thread(target=robot1_task, args=(robots,))
    task2_thread = threading.Thread(target=robot2_task, args=(robots,))

    task1_thread.start()
    task2_thread.start()

    task1_thread.join()
    task2_thread.join()

    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})

    task_over = True
    time.sleep(5)