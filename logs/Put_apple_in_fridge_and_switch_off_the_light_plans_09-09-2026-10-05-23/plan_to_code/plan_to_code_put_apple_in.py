#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_apple_in_fridge_and_switch_off_the_light_plans_09-09-2026-10-05-23
Scene ID: pddl_generated
Task: Put apple in fridge and switch off the light
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def execute_task(robots):
    def robot1_task(robots):
        GoToObject(robots[0], 'Apple')
        PickupObject(robots[0], 'Apple')
        GoToObject(robots[0], 'Fridge')
        OpenObject(robots[0], 'Fridge')
        PutObject(robots[0], 'Apple', 'Fridge')
        CloseObject(robots[0], 'Fridge')

    def robot2_task(robots):
        GoToObject(robots[1], 'LightSwitch')
        SwitchOff(robots[1], 'LightSwitch')

    task1_thread = threading.Thread(target=robot1_task, args=(robots,))
    task2_thread = threading.Thread(target=robot2_task, args=(robots,))

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
