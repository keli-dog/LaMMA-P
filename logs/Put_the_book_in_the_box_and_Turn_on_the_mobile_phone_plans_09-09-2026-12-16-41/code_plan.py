def put_book_in_box(robots):
    GoToObject(robots[0], 'Book')
    PickupObject(robots[0], 'Book')
    GoToObject(robots[0], 'Box')
    PutObject(robots[0], 'Book', 'Box')

def turn_on_phone(robots):
    GoToObject(robots[1], 'CellPhone')
    SwitchOn(robots[1], 'CellPhone')

task1_thread = threading.Thread(target=put_book_in_box, args=(robots,))
task2_thread = threading.Thread(target=turn_on_phone, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True