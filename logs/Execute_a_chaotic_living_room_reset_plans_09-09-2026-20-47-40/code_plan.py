def execute_task(robots):
    def robot1_task():
        GoToObject(robots[0], 'Television')
        SwitchOff(robots[0], 'Television')
        GoToObject(robots[0], 'Drawer')
        CloseObject(robots[0], 'Drawer')
        GoToObject(robots[0], 'Book')
        PickupObject(robots[0], 'Book')
        GoToObject(robots[0], 'Shelf')
        PutObject(robots[0], 'Book', 'Shelf')

    def robot2_task():
        GoToObject(robots[1], 'FloorLamp')
        SwitchOff(robots[1], 'FloorLamp')
        GoToObject(robots[1], 'Drawer')
        CloseObject(robots[1], 'Drawer')
        GoToObject(robots[1], 'RemoteControl')
        PickupObject(robots[1], 'RemoteControl')
        GoToObject(robots[1], 'CoffeeTable')
        PutObject(robots[1], 'RemoteControl', 'CoffeeTable')
        GoToObject(robots[1], 'CoffeeTable')
        CleanObject(robots[1], 'CoffeeTable')

    def robot3_task():
        GoToObject(robots[2], 'Drawer')
        CloseObject(robots[2], 'Drawer')
        GoToObject(robots[2], 'Newspaper')
        PickupObject(robots[2], 'Newspaper')
        GoToObject(robots[2], 'SideTable')
        PutObject(robots[2], 'Newspaper', 'SideTable')
        GoToObject(robots[2], 'Pillow')
        PickupObject(robots[2], 'Pillow')
        GoToObject(robots[2], 'Sofa')
        PutObject(robots[2], 'Pillow', 'Sofa')
        GoToObject(robots[2], 'SideTable')
        CleanObject(robots[2], 'SideTable')
        GoToObject(robots[2], 'SideTable')
        CleanObject(robots[2], 'SideTable')

    t1 = threading.Thread(target=robot1_task)
    t2 = threading.Thread(target=robot2_task)
    t3 = threading.Thread(target=robot3_task)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})