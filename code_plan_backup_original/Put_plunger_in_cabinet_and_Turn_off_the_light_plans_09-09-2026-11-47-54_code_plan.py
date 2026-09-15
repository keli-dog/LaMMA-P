def execute_task(robots):
    def task_plunger(robots):
        GoToObject(robots[0], 'Plunger')
        PickupObject(robots[0], 'Plunger')
        GoToObject(robots[0], 'Cabinet')
        OpenObject(robots[0], 'Cabinet')
        PutObject(robots[0], 'Plunger', 'Cabinet')
        CloseObject(robots[0], 'Cabinet')

    def task_light(robots):
        GoToObject(robots[1], 'LightSwitch')
        SwitchOff(robots[1], 'LightSwitch')

    task1_thread = threading.Thread(target=task_plunger, args=(robots,))
    task2_thread = threading.Thread(target=task_light, args=(robots,))

    task1_thread.start()
    task2_thread.start()

    task1_thread.join()
    task2_thread.join()

    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})

    task_over = True