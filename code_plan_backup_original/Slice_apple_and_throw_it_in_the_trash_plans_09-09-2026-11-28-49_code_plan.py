def execute_task():
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'CounterTop')
    SliceObject(robots[0], 'Apple')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'Apple', 'GarbageCan')

action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)