def execute_task(robots):
    def turn_on_faucet(robots):
        GoToObject(robots[1], 'Faucet')
        SwitchOn(robots[1], 'Faucet')

    def dispose_toilet_paper(robots):
        GoToObject(robots[2], 'ToiletPaper')
        PickupObject(robots[2], 'ToiletPaper')
        GoToObject(robots[2], 'GarbageCan')
        PutObject(robots[2], 'ToiletPaper', 'GarbageCan')

    task1_thread = threading.Thread(target=turn_on_faucet, args=(robots,))
    task2_thread = threading.Thread(target=dispose_toilet_paper, args=(robots,))

    task1_thread.start()
    task2_thread.start()

    task1_thread.join()
    task2_thread.join()

    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})

    task_over = True
    time.sleep(5)