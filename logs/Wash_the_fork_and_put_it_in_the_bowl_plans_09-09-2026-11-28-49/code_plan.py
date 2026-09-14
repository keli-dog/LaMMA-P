def wash_fork(robots):
    GoToObject(robots[0], 'Fork')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'SinkBasin')
    CleanObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Bowl')
    PutObject(robots[0], 'Fork', 'Bowl')

def execute_task():
    task_thread = threading.Thread(target=wash_fork, args=(robots,))
    task_thread.start()
    task_thread.join()
    action_queue.append({'action':'Done'})
    task_over = True
    time.sleep(5)