def break_cellphone(robots):
    GoToObject(robots[1], 'CellPhone')
    BreakObject(robots[1], 'CellPhone')

def close_blinds(robots):
    GoToObject(robots[0], 'Blinds')
    CloseObject(robots[0], 'Blinds')

def dispose_book(robots):
    GoToObject(robots[2], 'Book')
    PickupObject(robots[2], 'Book')
    GoToObject(robots[2], 'GarbageCan')
    PutObject(robots[2], 'Book', 'GarbageCan')

task1_thread = threading.Thread(target=break_cellphone, args=(robots,))
task2_thread = threading.Thread(target=close_blinds, args=(robots,))
task3_thread = threading.Thread(target=dispose_book, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True