def prepare_hot_water(robots):
    GoToObject(robots[0], 'Faucet')
    SwitchOn(robots[0], 'Faucet')
    GoToObject(robots[0], 'Bathtub')
    SwitchOff(robots[0], 'Faucet')

def dispose_toiletpaper(robots):
    GoToObject(robots[1], 'ToiletPaper')
    PickupObject(robots[1], 'ToiletPaper')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'ToiletPaper', 'GarbageCan')

task1_thread = threading.Thread(target=prepare_hot_water, args=(robots,))
task2_thread = threading.Thread(target=dispose_toiletpaper, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)