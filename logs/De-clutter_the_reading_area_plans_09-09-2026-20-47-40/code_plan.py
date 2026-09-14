def declutter_reading_area(robots):
    GoToObject(robots[3], 'Book')
    GoToObject(robots[0], 'Newspaper')
    GoToObject(robots[0], 'RemoteControl')
    GoToObject(robots[2], 'Pen')
    
    PickupObject(robots[3], 'Book')
    PickupObject(robots[0], 'Newspaper')
    PickupObject(robots[0], 'RemoteControl')
    PickupObject(robots[2], 'Pen')
    
    GoToObject(robots[3], 'Shelf')
    GoToObject(robots[0], 'GarbageCan')
    GoToObject(robots[0], 'SideTable')
    GoToObject(robots[2], 'Drawer')
    
    PutObject(robots[3], 'Book', 'Shelf')
    PutObject(robots[0], 'Newspaper', 'GarbageCan')
    PutObject(robots[0], 'RemoteControl', 'SideTable')
    OpenObject(robots[2], 'Drawer')
    
    PutObject(robots[2], 'Pen', 'Drawer')
    CloseObject(robots[2], 'Drawer')

def execute_task():
    declutter_reading_area(robots)
    action_queue.append({'action':'Done'})
    task_over = True