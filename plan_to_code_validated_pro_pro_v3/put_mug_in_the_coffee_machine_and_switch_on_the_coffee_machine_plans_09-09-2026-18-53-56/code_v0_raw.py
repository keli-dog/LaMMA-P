def put_mug_and_switch_on(robots):
    GoToObject(robots[0], 'Mug')
    PickupObject(robots[0], 'Mug')
    GoToObject(robots[0], 'CoffeeMachine')
    PutObject(robots[0], 'Mug', 'CoffeeMachine')
    GoToObject(robots[1], 'CoffeeMachine')
    SwitchOn(robots[1], 'CoffeeMachine')

task1_thread = threading.Thread(target=put_mug_and_switch_on, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)