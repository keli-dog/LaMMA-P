def chill_apple(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Apple', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def wash_knife(robots):
    GoToObject(robots[1], 'Knife')
    PickupObject(robots[1], 'Knife')
    GoToObject(robots[1], 'Sink')
    CleanObject(robots[1], 'Knife')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'Knife', 'CounterTop')

task1_thread = threading.Thread(target=chill_apple, args=(robots,))
task2_thread = threading.Thread(target=wash_knife, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)