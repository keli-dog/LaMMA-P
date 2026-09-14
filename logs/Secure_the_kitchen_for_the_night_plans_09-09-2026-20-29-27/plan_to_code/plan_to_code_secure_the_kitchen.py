#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Secure_the_kitchen_for_the_night_plans_09-09-2026-20-29-27
Scene ID: pddl_generated
Task: Secure the kitchen for the night
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def store_eggs(robots):
    GoToObject(robots[0], 'Egg')
    PickupObject(robots[0], 'Egg')
    GoToObject(robots[0], 'Fridge')
    OpenObject(robots[0], 'Fridge')
    PutObject(robots[0], 'Egg', 'Fridge')
    CloseObject(robots[0], 'Fridge')

def clean_plate(robots):
    GoToObject(robots[1], 'Plate')
    PickupObject(robots[1], 'Plate')
    CleanObject(robots[1], 'Plate')
    GoToObject(robots[1], 'Cabinet')
    OpenObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Plate', 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

def close_cabinets(robots):
    GoToObject(robots[1], 'Cabinet')
    CloseObject(robots[1], 'Cabinet')

def turn_off_appliances(robots):
    GoToObject(robots[0], 'CoffeeMachine')
    SwitchOff(robots[0], 'CoffeeMachine')
    GoToObject(robots[0], 'Microwave')
    SwitchOff(robots[0], 'Microwave')

def clean_cup(robots):
    GoToObject(robots[1], 'Cup')
    PickupObject(robots[1], 'Cup')
    CleanObject(robots[1], 'Cup')
    GoToObject(robots[1], 'Cabinet')
    PutObject(robots[1], 'Cup', 'Cabinet')

def turn_off_lights(robots):
    GoToObject(robots[0], 'LightSwitch')
    SwitchOff(robots[0], 'LightSwitch')

task1_thread = threading.Thread(target=store_eggs, args=(robots,))
task2_thread = threading.Thread(target=clean_plate, args=(robots,))
task3_thread = threading.Thread(target=close_cabinets, args=(robots,))

task1_thread.start()
task2_thread.start()
task3_thread.start()

task1_thread.join()
task2_thread.join()
task3_thread.join()

task4_thread = threading.Thread(target=turn_off_appliances, args=(robots,))
task5_thread = threading.Thread(target=clean_cup, args=(robots,))

task4_thread.start()
task5_thread.start()

task4_thread.join()
task5_thread.join()

turn_off_lights(robots)

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
