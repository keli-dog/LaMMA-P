def put_watch_keychain_in_drawer(robots):
    GoToObject(robots[0], 'Watch')
    GoToObject(robots[1], 'KeyChain')
    PickupObject(robots[0], 'Watch')
    PickupObject(robots[1], 'KeyChain')
    GoToObject(robots[0], 'Drawer')
    GoToObject(robots[1], 'Drawer')
    OpenObject(robots[0], 'Drawer')
    OpenObject(robots[1], 'Drawer')
    PutObject(robots[0], 'Watch', 'Drawer')
    PutObject(robots[1], 'KeyChain', 'Drawer')
    CloseObject(robots[0], 'Drawer')
    CloseObject(robots[1], 'Drawer')

task1_thread = threading.Thread(target=put_watch_keychain_in_drawer, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True