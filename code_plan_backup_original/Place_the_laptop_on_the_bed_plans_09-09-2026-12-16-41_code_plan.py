def place_laptop_on_bed(robots):
    GoToObject(robots[0], 'Laptop')
    PickupObject(robots[0], 'Laptop')
    GoToObject(robots[0], 'Bed')
    PutObject(robots[0], 'Laptop', 'Bed')
    action_queue.append({'action':'Done'})
    task_over = True