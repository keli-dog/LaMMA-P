def organize_heavy_objects(robots):
    GoToObject(robots[0], 'ArmChair')
    PickupObject(robots[0], 'ArmChair')
    GoToObject(robots[0], 'Dresser')
    PutObject(robots[0], 'ArmChair', 'Dresser')
    GoToObject(robots[0], 'Sofa')
    PickupObject(robots[0], 'Sofa')
    GoToObject(robots[0], 'Dresser')
    PutObject(robots[0], 'Sofa', 'Dresser')
    GoToObject(robots[0], 'CoffeeTable')
    PickupObject(robots[0], 'CoffeeTable')
    GoToObject(robots[0], 'SideTable')
    PutObject(robots[0], 'CoffeeTable', 'SideTable')

def organize_small_objects(robots):
    GoToObject(robots[1], 'Book')
    PickupObject(robots[1], 'Book')
    GoToObject(robots[1], 'Shelf')
    PutObject(robots[1], 'Book', 'Shelf')
    GoToObject(robots[1], 'Laptop')
    PickupObject(robots[1], 'Laptop')
    GoToObject(robots[1], 'Shelf')
    PutObject(robots[1], 'Laptop', 'Shelf')
    GoToObject(robots[1], 'Vase')
    PickupObject(robots[1], 'Vase')
    GoToObject(robots[1], 'Shelf')
    PutObject(robots[1], 'Vase', 'Shelf')
    GoToObject(robots[1], 'RemoteControl')
    PickupObject(robots[1], 'RemoteControl')
    GoToObject(robots[1], 'Drawer')
    PutObject(robots[1], 'RemoteControl', 'Drawer')

task1_thread = threading.Thread(target=organize_heavy_objects, args=(robots,))
task2_thread = threading.Thread(target=organize_small_objects, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)