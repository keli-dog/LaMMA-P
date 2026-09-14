def wash_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    CleanObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'CounterTop')
    PickupObject(robots[0], 'Lettuce')
    PutObject(robots[0], 'Lettuce', 'CounterTop')

task_thread = threading.Thread(target=wash_lettuce, args=(robots,))
task_thread.start()
task_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)