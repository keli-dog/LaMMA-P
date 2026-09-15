def put_pen(robots):
    GoToObject(robots[0], 'Pen')
    PickupObject(robots[0], 'Pen')
    GoToObject(robots[0], 'Bed')
    PutObject(robots[0], 'Pen', 'Bed')

def put_book(robots):
    GoToObject(robots[1], 'Book')
    PickupObject(robots[1], 'Book')
    GoToObject(robots[1], 'Bed')
    PutObject(robots[1], 'Book', 'Bed')

task1_thread = threading.Thread(target=put_pen, args=(robots,))
task2_thread = threading.Thread(target=put_book, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True