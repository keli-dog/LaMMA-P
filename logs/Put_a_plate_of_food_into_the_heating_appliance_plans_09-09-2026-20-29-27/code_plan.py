def heat_food(robots):
    GoToObject(robots[0], 'Plate')
    PickupObject(robots[0], 'Plate')
    GoToObject(robots[0], 'Microwave')
    OpenObject(robots[0], 'Microwave')
    PutObject(robots[0], 'Plate', 'Microwave')
    CloseObject(robots[0], 'Microwave')
    SwitchOn(robots[0], 'Microwave')

task_thread = threading.Thread(target=heat_food, args=(robots,))
task_thread.start()
task_thread.join()

action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)