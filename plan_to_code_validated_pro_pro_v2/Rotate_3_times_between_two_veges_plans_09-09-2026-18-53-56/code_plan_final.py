def rotate_between_vegetables(robots):
    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Tomato')
    GoToObject(robots[0], 'Lettuce')
    action_queue.append({'action':'Done'})
    task_over = True