#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_the_Box_on_the_sofa_and_the_bowl_in_the_box_plans_09-09-2026-10-21-28
Scene ID: pddl_generated
Task: Put the Box on the sofa and the bowl in the box
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def put_box_on_sofa_and_bowl_in_box(robots):
    GoToObject(robots[0], 'Box')
    PickupObject(robots[0], 'Box')
    GoToObject(robots[0], 'Sofa')
    PutObject(robots[0], 'Box', 'Sofa')
    GoToObject(robots[0], 'Bowl')
    PickupObject(robots[0], 'Bowl')
    GoToObject(robots[0], 'Box')
    PutObject(robots[0], 'Bowl', 'Box')

def execute_task():
    put_box_on_sofa_and_bowl_in_box([robot0])

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
