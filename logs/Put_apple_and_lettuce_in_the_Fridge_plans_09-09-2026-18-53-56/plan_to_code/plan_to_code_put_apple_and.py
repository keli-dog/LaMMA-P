#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_apple_and_lettuce_in_the_Fridge_plans_09-09-2026-18-53-56
Scene ID: pddl_generated
Task: Put apple and lettuce in the Fridge
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def put_apple_in_fridge(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Apple', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def put_lettuce_in_fridge(robots):
    GoToObject(robots[1], 'Lettuce')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Lettuce', 'Fridge')
    CloseObject(robots[1], 'Fridge')

task1_thread = threading.Thread(target=put_apple_in_fridge, args=(robots,))
task2_thread = threading.Thread(target=put_lettuce_in_fridge, args=(robots,))

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
