def slice_lettuce_and_put_in_fridge(robots):
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Lettuce')
    SliceObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Lettuce', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def execute_task():
    slice_lettuce_and_put_in_fridge(robots)
    action_queue.append({'action':'Done'})
    task_over = True
    time.sleep(5)