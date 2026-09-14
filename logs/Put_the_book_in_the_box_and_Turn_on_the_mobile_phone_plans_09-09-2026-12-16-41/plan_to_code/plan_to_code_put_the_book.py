#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_the_book_in_the_box_and_Turn_on_the_mobile_phone_plans_09-09-2026-12-16-41
Scene ID: pddl_generated
Task: Put the book in the box and Turn on the mobile phone
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def put_book_in_box(robots):
    GoToObject(robots[0], 'Book')
    PickupObject(robots[0], 'Book')
    GoToObject(robots[0], 'Box')
    PutObject(robots[0], 'Book', 'Box')

def turn_on_phone(robots):
    GoToObject(robots[1], 'CellPhone')
    SwitchOn(robots[1], 'CellPhone')

task1_thread = threading.Thread(target=put_book_in_box, args=(robots,))
task2_thread = threading.Thread(target=turn_on_phone, args=(robots,))

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
