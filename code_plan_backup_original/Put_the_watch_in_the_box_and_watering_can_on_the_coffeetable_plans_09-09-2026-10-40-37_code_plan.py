def execute_task(robots):
    task1_thread = threading.Thread(target=put_watch_in_box, args=(robots,))
    task2_thread = threading.Thread(target=put_wateringcan_on_coffeetable, args=(robots,))
    task1_thread.start()
    task2_thread.start()
    task1_thread.join()
    task2_thread.join()
    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})
    task_over = True

def put_watch_in_box(robots):
    GoToObject(robots[0], 'Watch')
    PickupObject(robots[0], 'Watch')
    GoToObject(robots[0], 'Box')
    PutObject(robots[0], 'Watch', 'Box')

def put_wateringcan_on_coffeetable(robots):
    GoToObject(robots[1], 'WateringCan')
    PickupObject(robots[1], 'WateringCan')
    GoToObject(robots[1], 'CoffeeTable')
    PutObject(robots[1], 'WateringCan', 'CoffeeTable')