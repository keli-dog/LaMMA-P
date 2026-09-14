#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_two_vegetables_in_the_fridge_parallely_plans_09-09-2026-11-28-49
Scene ID: pddl_generated
Task: Put two vegetables in the fridge parallely
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def put_lettuce_in_fridge(robots):
    GoToObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Lettuce', 'Fridge')

def put_tomato_in_fridge(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Tomato', 'Fridge')
    CloseObject(robots[1], 'Fridge')

task1_thread = threading.Thread(target=put_lettuce_in_fridge, args=(robots,))
task2_thread = threading.Thread(target=put_tomato_in_fridge, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
