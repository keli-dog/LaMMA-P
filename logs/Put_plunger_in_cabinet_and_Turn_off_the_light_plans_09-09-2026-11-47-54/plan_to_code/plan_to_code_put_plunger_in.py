#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_plunger_in_cabinet_and_Turn_off_the_light_plans_09-09-2026-11-47-54
Scene ID: pddl_generated
Task: Put plunger in cabinet and Turn off the light
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def execute_task(robots):
    def task_plunger(robots):
        GoToObject(robots[0], 'Plunger')
        PickupObject(robots[0], 'Plunger')
        GoToObject(robots[0], 'Cabinet')
        OpenObject(robots[0], 'Cabinet')
        PutObject(robots[0], 'Plunger', 'Cabinet')
        CloseObject(robots[0], 'Cabinet')

    def task_light(robots):
        GoToObject(robots[1], 'LightSwitch')
        SwitchOff(robots[1], 'LightSwitch')

    task1_thread = threading.Thread(target=task_plunger, args=(robots,))
    task2_thread = threading.Thread(target=task_light, args=(robots,))

    task1_thread.start()
    task2_thread.start()

    task1_thread.join()
    task2_thread.join()

    action_queue.append({'action':'Done'})
    action_queue.append({'action':'Done'})

    task_over = True

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
