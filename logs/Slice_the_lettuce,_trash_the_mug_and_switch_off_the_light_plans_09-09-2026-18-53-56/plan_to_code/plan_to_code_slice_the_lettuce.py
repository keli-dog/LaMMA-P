#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Slice_the_lettuce,_trash_the_mug_and_switch_off_the_light_plans_09-09-2026-18-53-56
Scene ID: pddl_generated
Task: Slice the lettuce, trash the mug and switch off the light
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def slice_lettuce(robots):
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Lettuce')
    SliceObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'CounterTop')
    PutObject(robots[0], 'Knife', 'CounterTop')

def trash_mug(robots):
    GoToObject(robots[1], 'Mug')
    PickupObject(robots[1], 'Mug')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Mug', 'GarbageCan')

def switch_off_light(robots):
    GoToObject(robots[2], 'LightSwitch')
    SwitchOff(robots[2], 'LightSwitch')

task1_thread = threading.Thread(target=slice_lettuce, args=(robots,))
task2_thread = threading.Thread(target=trash_mug, args=(robots,))
task3_thread = threading.Thread(target=switch_off_light, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
