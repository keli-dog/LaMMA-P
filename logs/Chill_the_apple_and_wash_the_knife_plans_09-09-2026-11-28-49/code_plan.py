def chill_apple_wash_knife(robots):
    GoToObject(robots[1], 'Knife')
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[1], 'Knife')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[1], 'Sink')
    GoToObject(robots[0], 'Fridge')
    CleanObject(robots[1], 'Knife')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Apple', 'Fridge')
    CloseObject(robots[0], 'Fridge')
    PutObject(robots[1], 'Knife', 'CounterTop')

task1_thread = threading.Thread(target=chill_apple_wash_knife, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)