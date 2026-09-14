def put_mug_and_switch_on(robots):
    GoToObject(robots[0], 'Mug')
    time.sleep(0.5)
    PickupObject(robots[0], 'Mug')
    time.sleep(0.5)
    GoToObject(robots[0], 'CoffeeMachine')
    time.sleep(0.5)
    PutObject(robots[0], 'Mug', 'CoffeeMachine')
    time.sleep(0.5)
    SwitchOn(robots[0], 'CoffeeMachine')

put_mug_and_switch_on(robots)
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)