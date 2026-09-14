import threading
import time

def slice_and_store(robots):
    global task_over
    
    def robot1_task(robot):
        GoToObject(robot, 'Knife')
        PickupObject(robot, 'Knife')
        GoToObject(robot, 'Lettuce')
        SliceObject(robot, 'Lettuce')
        PutObject(robot, 'Knife', 'CounterTop')
        GoToObject(robot, 'Lettuce')
        PickupObject(robot, 'Lettuce')
        GoToObject(robot, 'Fridge')
        OpenObject(robot, 'Fridge')
        PutObject(robot, 'Lettuce', 'Fridge')
        CloseObject(robot, 'Fridge')
        action_queue.append({'action':'Done'})

    def robot2_task(robot):
        time.sleep(2)  # Wait for robot1 to finish with knife
        GoToObject(robot, 'ButterKnife')
        PickupObject(robot, 'ButterKnife')
        GoToObject(robot, 'Tomato')
        SliceObject(robot, 'Tomato')
        PutObject(robot, 'ButterKnife', 'CounterTop')
        GoToObject(robot, 'Tomato')
        PickupObject(robot, 'Tomato')
        GoToObject(robot, 'Fridge')
        OpenObject(robot, 'Fridge')
        PutObject(robot, 'Tomato', 'Fridge')
        CloseObject(robot, 'Fridge')
        action_queue.append({'action':'Done'})

    task1_thread = threading.Thread(target=robot1_task, args=(robots[0],))
    task2_thread = threading.Thread(target=robot2_task, args=(robots[1],))
    task1_thread.start()
    task2_thread.start()
    task1_thread.join()
    task2_thread.join()
    time.sleep(5)
    task_over = True