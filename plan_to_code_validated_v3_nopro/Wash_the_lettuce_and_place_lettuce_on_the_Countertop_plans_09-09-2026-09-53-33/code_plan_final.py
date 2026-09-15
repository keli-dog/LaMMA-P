def wash_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'SinkBasin')
    SwitchOn(robots[0], 'Faucet')
    CleanObject(robots[0], 'Lettuce')
    SwitchOff(robots[0], 'Faucet')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Lettuce', 'CounterTop')

task1_thread = threading.Thread(target=wash_lettuce, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)