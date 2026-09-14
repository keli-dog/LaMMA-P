#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Parallely_put_pen_and_book_on_the_bed_plans_09-09-2026-19-33-20
Scene ID: pddl_generated
Task: Parallely put pen and book on the bed
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def put_pen(robots):
    GoToObject(robots[0], 'Pen')
    PickupObject(robots[0], 'Pen')
    GoToObject(robots[0], 'Bed')
    PutObject(robots[0], 'Pen', 'Bed')

def put_book(robots):
    GoToObject(robots[1], 'Book')
    PickupObject(robots[1], 'Book')
    GoToObject(robots[1], 'Bed')
    PutObject(robots[1], 'Book', 'Bed')

task1_thread = threading.Thread(target=put_pen, args=(robots,))
task2_thread = threading.Thread(target=put_book, args=(robots,))

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
