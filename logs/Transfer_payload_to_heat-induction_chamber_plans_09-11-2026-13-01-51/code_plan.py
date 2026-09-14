def execute_task(robots):
    GoToObject(robots[1], 'Microwave')
    GoToObject(robots[0], 'Mug')
    OpenObject(robots[1], 'Microwave')
    PickupObject(robots[0], 'Mug')
    GoToObject(robots[0], 'Microwave')
    PutObject(robots[0], 'Mug', 'Microwave')
    CloseObject(robots[1], 'Microwave')