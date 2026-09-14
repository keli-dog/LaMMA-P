#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Microwave_a_plate_containing_a_egg_and_a_tomato_plans_09-09-2026-18-53-56
Scene ID: pddl_generated
Task: Microwave a plate containing a egg and a tomato
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def prepare_plate(robots):
    GoToObject(robots[1], 'Plate')
    PickupObject(robots[1], 'Plate')
    GoToObject(robots[1], 'Microwave')
    PutObject(robots[1], 'Plate', 'Microwave')

def prepare_egg(robots):
    GoToObject(robots[1], 'Egg')
    PickupObject(robots[1], 'Egg')
    GoToObject(robots[1], 'Microwave')
    PutObject(robots[1], 'Egg', 'Plate')

def prepare_tomato(robots):
    GoToObject(robots[1], 'Tomato')
    PickupObject(robots[1], 'Tomato')
    GoToObject(robots[1], 'Microwave')
    PutObject(robots[1], 'Tomato', 'Plate')

def microwave_food(robots):
    GoToObject(robots[2], 'Microwave')
    SwitchOn(robots[2], 'Microwave')
    time.sleep(30)
    SwitchOff(robots[2], 'Microwave')

plate_thread = threading.Thread(target=prepare_plate, args=(robots,))
egg_thread = threading.Thread(target=prepare_egg, args=(robots,))
tomato_thread = threading.Thread(target=prepare_tomato, args=(robots,))

plate_thread.start()
plate_thread.join()

egg_thread.start()
tomato_thread.start()
egg_thread.join()
tomato_thread.join()

microwave_thread = threading.Thread(target=microwave_food, args=(robots,))
microwave_thread.start()
microwave_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
