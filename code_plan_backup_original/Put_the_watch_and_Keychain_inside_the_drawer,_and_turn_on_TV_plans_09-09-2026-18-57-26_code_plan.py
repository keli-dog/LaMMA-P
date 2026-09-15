def put_watch_in_drawer(robots):
    GoToObject(robots[0], 'Watch')
    PickupObject(robots[0], 'Watch')
    GoToObject(robots[0], 'Drawer')
    OpenObject(robots[0], 'Drawer')
    PutObject(robots[0], 'Watch', 'Drawer')
    CloseObject(robots[0], 'Drawer')

def put_keychain_in_drawer(robots):
    GoToObject(robots[1], 'KeyChain')
    PickupObject(robots[1], 'KeyChain')
    GoToObject(robots[1], 'Drawer')
    PutObject(robots[1], 'KeyChain', 'Drawer')

def turn_on_tv(robots):
    GoToObject(robots[2], 'Television')
    SwitchOn(robots[2], 'Television')

def execute_task():
    task1_thread = threading.Thread(target=put_watch_in_drawer, args=(robots,))
    task2_thread = threading.Thread(target=put_keychain_in_drawer, args=(robots,))
    task3_thread = threading.Thread(target=turn_on_tv, args=(robots,))

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