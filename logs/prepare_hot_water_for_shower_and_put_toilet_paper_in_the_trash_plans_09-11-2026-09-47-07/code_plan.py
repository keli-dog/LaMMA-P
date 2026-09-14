def execute_task(robots):
    GoToObject(robots[1], 'Faucet')
    GoToObject(robots[2], 'CounterTop')
    SwitchOn(robots[1], 'Faucet')
    PickupObject(robots[2], 'ToiletPaper')
    GoToObject(robots[1], 'LightSwitch')
    GoToObject(robots[2], 'GarbageCan')
    SwitchOn(robots[1], 'LightSwitch')
    PutObject(robots[2], 'ToiletPaper', 'GarbageCan')