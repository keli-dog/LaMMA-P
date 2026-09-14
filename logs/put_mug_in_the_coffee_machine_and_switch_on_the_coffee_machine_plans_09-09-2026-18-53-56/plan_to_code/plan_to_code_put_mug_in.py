#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: put_mug_in_the_coffee_machine_and_switch_on_the_coffee_machine_plans_09-09-2026-18-53-56
Scene ID: pddl_generated
Task: put mug in the coffee machine and switch on the coffee machine
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def put_mug_and_switch_on(robots):
    GoToObject(robots[0], 'Mug')
    PickupObject(robots[0], 'Mug')
    GoToObject(robots[0], 'CoffeeMachine')
    PutObject(robots[0], 'Mug', 'CoffeeMachine')
    GoToObject(robots[1], 'CoffeeMachine')
    SwitchOn(robots[1], 'CoffeeMachine')

task1_thread = threading.Thread(target=put_mug_and_switch_on, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
