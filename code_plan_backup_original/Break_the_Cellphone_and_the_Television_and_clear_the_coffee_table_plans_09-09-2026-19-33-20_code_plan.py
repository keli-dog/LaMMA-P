def break_cellphone(robots):
    GoToObject(robots[0], 'CellPhone')
    BreakObject(robots[0], 'CellPhone')

def clear_desk(robots):
    GoToObject(robots[1], 'Desk')
    PickupObject(robots[1], 'Book')
    GoToObject(robots[1], 'ShelvingUnit')
    PutObject(robots[1], 'Book', 'ShelvingUnit')
    GoToObject(robots[1], 'Desk')
    PickupObject(robots[1], 'Laptop')
    GoToObject(robots[1], 'ShelvingUnit')
    PutObject(robots[1], 'Laptop', 'ShelvingUnit')
    GoToObject(robots[1], 'Desk')
    PickupObject(robots[1], 'Mug')
    GoToObject(robots[1], 'ShelvingUnit')
    PutObject(robots[1], 'Mug', 'ShelvingUnit')

task1_thread = threading.Thread(target=break_cellphone, args=(robots,))
task2_thread = threading.Thread(target=clear_desk, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)