def break_vase(robots):
    GoToObject(robots[0], 'Vase')
    BreakObject(robots[0], 'Vase')

def turn_on_tv(robots):
    GoToObject(robots[1], 'Television')
    SwitchOn(robots[1], 'Television')

task1_thread = threading.Thread(target=break_vase, args=(robots,))
task2_thread = threading.Thread(target=turn_on_tv, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True