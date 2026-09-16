def slice_apple(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Apple')
    SliceObject(robots[0], 'Apple')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Knife', 'CounterTop')
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'Apple', 'GarbageCan')

def slice_lettuce(robots):
    time.sleep(2)  # Increased delay to avoid knife contention
    GoToObject(robots[1], 'Lettuce')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'ButterKnife')  # Use different knife
    PickupObject(robots[1], 'ButterKnife')
    GoToObject(robots[1], 'Lettuce')
    SliceObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'CounterTop')
    PutObject(robots[1], 'ButterKnife', 'CounterTop')
    GoToObject(robots[1], 'Lettuce')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Lettuce', 'GarbageCan')

task1_thread = threading.Thread(target=slice_apple, args=(robots,))
task2_thread = threading.Thread(target=slice_lettuce, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
if not task1_thread.is_alive() and not task2_thread.is_alive():  # Check both threads completed
    task_over = True
time.sleep(5)