#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_the_book_in_the_box,_turn_on_the_mobile_phone,_and_clear_the_desk_plans_09-09-2026-19-33-20
Scene ID: pddl_generated
Task: Put the book in the box, turn on the mobile phone, and clear the desk
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def execute_task(robots):
    def subtask1(robots):
        GoToObject(robots[0], 'Book')
        PickupObject(robots[0], 'Book')
        GoToObject(robots[0], 'Box')
        PutObject(robots[0], 'Book', 'Box')

    def subtask2(robots):
        GoToObject(robots[1], 'CellPhone')
        SwitchOn(robots[1], 'CellPhone')

    def subtask3(robots):
        GoToObject(robots[2], 'Desk')
        PickupObject(robots[2], 'Mug')
        GoToObject(robots[2], 'Shelf')
        PutObject(robots[2], 'Mug', 'Shelf')

    task1_thread = threading.Thread(target=subtask1, args=(robots,))
    task2_thread = threading.Thread(target=subtask2, args=(robots,))
    task3_thread = threading.Thread(target=subtask3, args=(robots,))

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
