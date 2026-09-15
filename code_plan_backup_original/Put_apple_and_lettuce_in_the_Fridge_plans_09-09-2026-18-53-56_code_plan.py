def put_apple(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Apple', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def put_lettuce(robots):
    GoToObject(robots[1], 'Lettuce')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'Fridge')
    time.sleep(3)
    OpenObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Lettuce', 'Fridge')
    CloseObject(robots[1], 'Fridge')

task1_thread = threading.Thread(target=put_apple, args=(robots,))
task2_thread = threading.Thread(target=put_lettuce, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)