def wash_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    CleanObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'CounterTop')
    PickupObject(robots[0], 'Lettuce')
    PutObject(robots[0], 'Lettuce', 'CounterTop')

task1_thread = threading.Thread(target=wash_lettuce, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)