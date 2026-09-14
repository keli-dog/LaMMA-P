#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Throw_the_Spatula_in_the_trash_plans_09-09-2026-09-53-33
Scene ID: pddl_generated
Task: Throw the Spatula in the trash
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def throw_spatula(robots):
    GoToObject(robots[0], 'Spatula')
    PickupObject(robots[0], 'Spatula')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'Spatula', 'GarbageCan')

def execute_task():
    throw_spatula([robot0])

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
