#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Put_a_plate_of_food_into_the_heating_appliance_plans_09-09-2026-20-29-27
Scene ID: pddl_generated
Task: Put a plate of food into the heating appliance
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def heat_food(robots):
    GoToObject(robots[0], 'Plate')
    PickupObject(robots[0], 'Plate')
    GoToObject(robots[0], 'Microwave')
    OpenObject(robots[0], 'Microwave')
    PutObject(robots[0], 'Plate', 'Microwave')
    CloseObject(robots[0], 'Microwave')
    SwitchOn(robots[0], 'Microwave')

task_thread = threading.Thread(target=heat_food, args=(robots,))
task_thread.start()
task_thread.join()

action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
