def stage_ingredients(robots):
    GoToObject(robots[0], 'DiningTable')
    GoToObject(robots[1], 'Fridge')
    PickupObject(robots[0], 'Apple')
    PickupObject(robots[1], 'Egg')
    GoToObject(robots[0], 'CounterTop')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[0], 'Apple', 'CounterTop')
    PutObject(robots[1], 'Egg', 'CounterTop')

def execute_task():
    stage_ingredients(robots)
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    task_over = True