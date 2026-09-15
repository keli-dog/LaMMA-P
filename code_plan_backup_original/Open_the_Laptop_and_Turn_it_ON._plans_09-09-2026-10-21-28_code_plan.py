def execute_task(robots):
    GoToObject(robots[0], 'Laptop')
    GoToObject(robots[1], 'Laptop')
    OpenObject(robots[0], 'Laptop')
    SwitchOn(robots[1], 'Laptop')