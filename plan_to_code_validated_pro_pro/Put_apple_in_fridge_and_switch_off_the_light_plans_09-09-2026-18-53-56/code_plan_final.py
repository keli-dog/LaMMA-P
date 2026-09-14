def put_apple_in_fridge(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Apple', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def switch_off_light(robots):
    GoToObject(robots[1], 'LightSwitch')
    SwitchOff(robots[1], 'LightSwitch')

task1_thread = threading.Thread(target=put_apple_in_fridge, args=(robots,))
task2_thread = threading.Thread(target=switch_off_light, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()
task_over = True
time.sleep(5)