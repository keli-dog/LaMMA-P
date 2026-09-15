def break_laptop(robots):
    GoToObject(robots[0], 'Laptop')
    BreakObject(robots[0], 'Laptop')

def break_alarmclock(robots):
    GoToObject(robots[0], 'AlarmClock')
    BreakObject(robots[0], 'AlarmClock')

def break_cellphone(robots):
    GoToObject(robots[0], 'CellPhone')
    BreakObject(robots[0], 'CellPhone')

def break_lightswitch(robots):
    GoToObject(robots[1], 'LightSwitch')
    BreakObject(robots[1], 'LightSwitch')

def break_desklamp(robots):
    GoToObject(robots[1], 'DeskLamp')
    BreakObject(robots[1], 'DeskLamp')

task1_thread = threading.Thread(target=break_laptop, args=(robots,))
task2_thread = threading.Thread(target=break_alarmclock, args=(robots,))
task3_thread = threading.Thread(target=break_cellphone, args=(robots,))
task4_thread = threading.Thread(target=break_lightswitch, args=(robots,))
task5_thread = threading.Thread(target=break_desklamp, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()
task4_thread.start()
task5_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()
task4_thread.join()
task5_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)