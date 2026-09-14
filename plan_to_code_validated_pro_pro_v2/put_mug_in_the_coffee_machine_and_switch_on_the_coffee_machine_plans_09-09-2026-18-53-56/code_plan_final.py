import threading
import time

def put_mug_and_switch_on(robots):
    GoToObject(robots[0], 'Mug')
    time.sleep(1)
    PickupObject(robots[0], 'Mug')
    time.sleep(1)
    GoToObject(robots[0], 'CoffeeMachine')
    time.sleep(1)
    PutObject(robots[0], 'Mug', 'CoffeeMachine')
    time.sleep(1)
    SwitchOn(robots[0], 'CoffeeMachine')
    time.sleep(1)

task1_thread = threading.Thread(target=put_mug_and_switch_on, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True