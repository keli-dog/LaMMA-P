#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Execute_a_deep_clean_and_waste_disposal_cycle_plans_09-09-2026-20-29-27
Scene ID: pddl_generated
Task: Execute a deep clean and waste disposal cycle
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def waste_disposal(robots):
    GoToObject(robots[0], 'GarbageBag')
    PickupObject(robots[0], 'GarbageBag')
    GoToObject(robots[0], 'GarbageCan')
    PutObject(robots[0], 'GarbageBag', 'GarbageCan')

def surface_cleaning(robots):
    GoToObject(robots[0], 'CounterTop')
    CleanObject(robots[0], 'CounterTop')
    GoToObject(robots[0], 'DiningTable')
    CleanObject(robots[0], 'DiningTable')

def object_organization(robots):
    GoToObject(robots[1], 'Plate')
    PickupObject(robots[1], 'Plate')
    GoToObject(robots[1], 'Cabinet')
    OpenObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Plate', 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

task1_thread = threading.Thread(target=waste_disposal, args=(robots,))
task2_thread = threading.Thread(target=surface_cleaning, args=(robots,))
task3_thread = threading.Thread(target=object_organization, args=(robots,))

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
