def execute_task(robots):
    def subtask1(robots):
        GoToObject(robots[0], 'Book')
        PickupObject(robots[0], 'Book')
        GoToObject(robots[0], 'Box')
        PutObject(robots[0], 'Book', 'Box')

    def subtask2(robots):
        GoToObject(robots[1], 'CellPhone')
        SwitchOn(robots[1], 'CellPhone')

    def subtask3(robots):
        GoToObject(robots[2], 'Desk')
        PickupObject(robots[2], 'Mug')
        GoToObject(robots[2], 'Shelf')
        PutObject(robots[2], 'Mug', 'Shelf')

    task1_thread = threading.Thread(target=subtask1, args=(robots,))
    task2_thread = threading.Thread(target=subtask2, args=(robots,))
    task3_thread = threading.Thread(target=subtask3, args=(robots,))

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