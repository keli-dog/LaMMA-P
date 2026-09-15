def break_cellphone(robots):
    GoToObject(robots[1], 'CellPhone')
    BreakObject(robots[1], 'CellPhone')

def close_blinds(robots):
    GoToObject(robots[0], 'Blinds')
    CloseObject(robots[0], 'Blinds')

task1_thread = threading.Thread(target=break_cellphone, args=(robots,))
task2_thread = threading.Thread(target=close_blinds, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)