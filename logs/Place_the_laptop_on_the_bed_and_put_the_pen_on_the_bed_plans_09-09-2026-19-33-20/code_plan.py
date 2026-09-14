def place_laptop_on_bed(robots):
    GoToObject(robots[0], 'Laptop')
    PickupObject(robots[0], 'Laptop')
    GoToObject(robots[0], 'Bed')
    PutObject(robots[0], 'Laptop', 'Bed')

def place_pen_on_bed(robots):
    GoToObject(robots[1], 'Pen')
    PickupObject(robots[1], 'Pen')
    GoToObject(robots[1], 'Bed')
    PutObject(robots[1], 'Pen', 'Bed')

task1_thread = threading.Thread(target=place_laptop_on_bed, args=(robots,))
task2_thread = threading.Thread(target=place_pen_on_bed, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)