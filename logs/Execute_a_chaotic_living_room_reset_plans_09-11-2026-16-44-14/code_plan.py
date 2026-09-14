def execute_task(robots):
    GoToObject(robots[0], 'FloorLamp')
    GoToObject(robots[1], 'Book')
    GoToObject(robots[2], 'Drawer')
    GoToObject(robots[3], 'Pillow')
    
    SwitchOff(robots[0], 'FloorLamp')
    PickupObject(robots[1], 'Book')
    CloseObject(robots[2], 'Drawer')
    PickupObject(robots[3], 'Pillow')
    
    GoToObject(robots[0], 'Laptop')
    GoToObject(robots[1], 'Shelf')
    GoToObject(robots[2], 'Drawer')
    GoToObject(robots[3], 'Sofa')
    
    SwitchOff(robots[0], 'Laptop')
    PutObject(robots[1], 'Book', 'Shelf')
    CloseObject(robots[2], 'Drawer')
    PutObject(robots[3], 'Pillow', 'Sofa')
    
    GoToObject(robots[0], 'LightSwitch')
    GoToObject(robots[1], 'RemoteControl')
    GoToObject(robots[2], 'Dresser')
    GoToObject(robots[3], 'Pillow')
    
    SwitchOff(robots[0], 'LightSwitch')
    PickupObject(robots[1], 'RemoteControl')
    CloseObject(robots[2], 'Dresser')
    PickupObject(robots[3], 'Pillow')
    
    GoToObject(robots[0], 'Television')
    GoToObject(robots[1], 'CoffeeTable')
    GoToObject(robots[3], 'Sofa')
    
    SwitchOff(robots[0], 'Television')
    PutObject(robots[1], 'RemoteControl', 'CoffeeTable')
    PutObject(robots[3], 'Pillow', 'Sofa')
    
    GoToObject(robots[1], 'Vase')
    
    PickupObject(robots[1], 'Vase')
    
    GoToObject(robots[1], 'SideTable')
    
    PutObject(robots[1], 'Vase', 'SideTable')