def put_mug_and_switch_on(robots):
    GoToObject(robots[1], 'CoffeeMachine')
    GoToObject(robots[2], 'CoffeeMachine')
    GoToObject(robots[1], 'Mug')
    PickupObject(robots[1], 'Mug')
    GoToObject(robots[1], 'CoffeeMachine')
    PutObject(robots[1], 'Mug', 'CoffeeMachine')
    SwitchOn(robots[2], 'CoffeeMachine')

task1_thread = threading.Thread(target=put_mug_and_switch_on, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)