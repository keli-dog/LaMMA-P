def execute_task(robots):
    action_queue = []
    task_over = False
    
    action_queue.append({'action':'GoToObject', 'robot':robots[0], 'object':'Knife'})
    action_queue.append({'action':'GoToObject', 'robot':robots[1], 'object':'Plate'})
    action_queue.append({'action':'PickupObject', 'robot':robots[0], 'object':'Knife'})
    action_queue.append({'action':'PickupObject', 'robot':robots[1], 'object':'Plate'})
    action_queue.append({'action':'GoToObject', 'robot':robots[0], 'object':'Potato'})
    action_queue.append({'action':'GoToObject', 'robot':robots[1], 'object':'Sink'})
    action_queue.append({'action':'SliceObject', 'robot':robots[0], 'object':'Potato'})
    action_queue.append({'action':'PutObject', 'robot':robots[1], 'object':'Plate', 'receptacle':'CounterTop'})
    action_queue.append({'action':'CleanObject', 'robot':robots[1], 'object':'Plate'})
    action_queue.append({'action':'PickupObject', 'robot':robots[1], 'object':'Plate'})
    action_queue.append({'action':'GoToObject', 'robot':robots[0], 'object':'Plate'})
    action_queue.append({'action':'PutObject', 'robot':robots[0], 'object':'Potato', 'receptacle':'Plate'})
    action_queue.append({'action':'Done'})
    task_over = True
    
    return action_queue, task_over