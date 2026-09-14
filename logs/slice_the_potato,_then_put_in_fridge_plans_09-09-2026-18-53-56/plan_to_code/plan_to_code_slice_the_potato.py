#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: slice_the_potato,_then_put_in_fridge_plans_09-09-2026-18-53-56
Scene ID: pddl_generated
Task: slice the potato, then put in fridge
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def slice_potato_and_store(robot):
    GoToObject(robot, 'Knife')
    PickupObject(robot, 'Knife')
    GoToObject(robot, 'Potato')
    SliceObject(robot, 'Potato')
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Knife', 'CounterTop')
    GoToObject(robot, 'Potato')
    PickupObject(robot, 'Potato')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Potato', 'Fridge')
    CloseObject(robot, 'Fridge')

def execute_task():
    slice_potato_and_store(robots[0])

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
