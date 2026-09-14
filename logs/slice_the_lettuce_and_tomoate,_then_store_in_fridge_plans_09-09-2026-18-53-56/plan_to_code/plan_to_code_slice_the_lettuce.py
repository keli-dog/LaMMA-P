#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: slice_the_lettuce_and_tomoate,_then_store_in_fridge_plans_09-09-2026-18-53-56
Scene ID: pddl_generated
Task: slice the lettuce and tomoate, then store in fridge
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
    PutObject(robots[0], 'Knife', 'CounterTop')

def slice_tomato(robots):
    GoToObject(robots[1], 'Knife')
    PickupObject(robots[1], 'Knife')
    GoToObject(robots[1], 'Tomato')
    SliceObject(robots[1], 'Tomato')
    PutObject(robots[1], 'Knife', 'CounterTop')

def store_lettuce(robots):
    GoToObject(robots[0], 'Lettuce')
    PickupObject(robots[0], 'Lettuce')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Lettuce', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def store_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Fridge')
    OpenObject(robots[1], 'Fridge')
    PutObject(robots[1], 'Tomato', 'Fridge')
    CloseObject(robots[1], 'Fridge')

task1_thread = threading.Thread(target=slice_lettuce, args=(robots,))
task2_thread = threading.Thread(target=slice_tomato, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

task3_thread = threading.Thread(target=store_lettuce, args=(robots,))
task4_thread = threading.Thread(target=store_tomato, args=(robots,))

task3_thread.start()
task4_thread.start()

task3_thread.join()
task4_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
