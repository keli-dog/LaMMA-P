def execute_task(robots):
    GoToObject(robots[0], 'Plate')
    GoToObject(robots[1], 'Microwave')
    PickupObject(robots[0], 'Plate')
    OpenObject(robots[1], 'Microwave')
    GoToObject(robots[0], 'Microwave')
    PutObject(robots[0], 'Plate', 'Microwave')
    CloseObject(robots[0], 'Microwave')