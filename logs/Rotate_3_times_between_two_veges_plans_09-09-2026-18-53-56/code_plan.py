def rotate_between_vegetables(robots):
    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'Lettuce')

def execute_task():
    rotate_thread = threading.Thread(target=rotate_between_vegetables, args=(robots,))
    rotate_thread.start()
    rotate_thread.join()
    action_queue.append({'action':'Done'})
    task_over = True
    time.sleep(5)