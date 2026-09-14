#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Trash_the_book_and_newspaper_plans_09-09-2026-10-40-37
Scene ID: pddl_generated
Task: Trash the book and newspaper
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def trash_book_and_newspaper(robots):
    GoToObject(robots[0], 'Book')
    GoToObject(robots[1], 'Newspaper')
    PickupObject(robots[0], 'Book')
    PickupObject(robots[1], 'Newspaper')
    GoToObject(robots[0], 'GarbageCan')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[0], 'Book', 'GarbageCan')
    PutObject(robots[1], 'Newspaper', 'GarbageCan')

task1_thread = threading.Thread(target=trash_book_and_newspaper, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
