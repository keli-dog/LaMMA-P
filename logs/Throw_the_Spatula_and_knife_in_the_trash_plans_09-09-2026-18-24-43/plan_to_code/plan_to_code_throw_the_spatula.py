#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Throw_the_Spatula_and_knife_in_the_trash_plans_09-09-2026-18-24-43
Scene ID: pddl_generated
Task: Throw the Spatula and knife in the trash
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

def throw_knife(robots):
    GoToObject(robots[1], 'Knife')
    PickupObject(robots[1], 'Knife')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Knife', 'GarbageCan')

task1_thread = threading.Thread(target=throw_spatula, args=(robots,))
task2_thread = threading.Thread(target=throw_knife, args=(robots,))

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
