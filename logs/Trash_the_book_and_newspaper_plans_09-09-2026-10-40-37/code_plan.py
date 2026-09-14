def trash_book_and_newspaper(robots):
    GoToObject(robots[0], 'Book')
    GoToObject(robots[1], 'Newspaper')
    PickupObject(robots[0], 'Book')
    PickupObject(robots[1], 'Newspaper')
    GoToObject(robots[0], 'GarbageCan')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[0], 'Book', 'GarbageCan')
    PutObject(robots[1], 'Newspaper', 'GarbageCan')

task1_thread = threading.Thread(target=trash_book_and_newspaper, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True