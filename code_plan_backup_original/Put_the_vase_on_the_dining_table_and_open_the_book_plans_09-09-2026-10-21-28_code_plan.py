def execute_task(robots):
    GoToObject(robots[0], 'Vase')
    GoToObject(robots[1], 'Book')
    PickupObject(robots[0], 'Vase')
    OpenObject(robots[1], 'Book')
    GoToObject(robots[0], 'DiningTable')
    PutObject(robots[0], 'Vase', 'DiningTable')