#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Slice_apple_and_lettuce_parallelly,_and_throw_them_in_the_trash_plans_09-09-2026-19-08-31
Scene ID: pddl_generated
Task: Slice apple and lettuce parallelly, and throw them in the trash
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def slice_apple(robots):
    GoToObject(robots[0], 'Apple')
    PickupObject(robots[0], 'Apple')
    GoToObject(robots[0], 'Knife')
    PickupObject(robots[0], 'Knife')
    GoToObject(robots[0], 'Apple')
    SliceObject(robots[0], 'Apple')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'Apple', 'GarbageCan')

def slice_lettuce(robots):
    GoToObject(robots[1], 'Lettuce')
    PickupObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'Knife')
    PickupObject(robots[1], 'Knife')
    GoToObject(robots[1], 'Lettuce')
    SliceObject(robots[1], 'Lettuce')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Lettuce', 'GarbageCan')

task1_thread = threading.Thread(target=slice_apple, args=(robots,))
task2_thread = threading.Thread(target=slice_lettuce, args=(robots,))

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
