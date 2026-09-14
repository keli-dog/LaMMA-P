#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Wash_the_fork_and_put_it_in_the_bowl_plans_09-09-2026-11-28-49
Scene ID: pddl_generated
Task: Wash the fork and put it in the bowl
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def wash_fork(robots):
    GoToObject(robots[0], 'Fork')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'SinkBasin')
    CleanObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Bowl')
    PutObject(robots[0], 'Fork', 'Bowl')

def execute_task():
    task_thread = threading.Thread(target=wash_fork, args=(robots,))
    task_thread.start()
    task_thread.join()
    action_queue.append({'action':'Done'})
    task_over = True
    time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
