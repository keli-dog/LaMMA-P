#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Execute_a_deep_clean_and_waste_disposal_cycle_plans_09-11-2026-13-01-51
Scene ID: pddl_generated
Task: Execute a deep clean and waste disposal cycle
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def clean_plate(robots):
    GoToObject(robots[0], 'Plate')
    CleanObject(robots[0], 'Plate')

def dispose_leftover_food(robots):
    GoToObject(robots[1], 'Bread')
    PickupObject(robots[1], 'Bread')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Bread', 'GarbageCan')

def clean_cup(robots):
    GoToObject(robots[0], 'Cup')
    CleanObject(robots[0], 'Cup')

def dispose_trash(robots):
    GoToObject(robots[1], 'Egg')
    PickupObject(robots[1], 'Egg')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'Egg', 'GarbageCan')

def clean_pan(robots):
    GoToObject(robots[0], 'Pan')
    CleanObject(robots[0], 'Pan')

def clean_pot(robots):
    GoToObject(robots[0], 'Pot')
    CleanObject(robots[0], 'Pot')

def clean_countertop(robots):
    GoToObject(robots[0], 'CounterTop')
    CleanObject(robots[0], 'CounterTop')

def dispose_garbage_bag(robots):
    GoToObject(robots[1], 'GarbageBag')
    PickupObject(robots[1], 'GarbageBag')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'GarbageBag', 'GarbageCan')

def clean_sink(robots):
    GoToObject(robots[0], 'Sink')
    CleanObject(robots[0], 'Sink')

def clean_garbagecan(robots):
    GoToObject(robots[0], 'GarbageCan')
    CleanObject(robots[0], 'GarbageCan')

task1_thread = threading.Thread(target=clean_plate, args=(robots,))
task2_thread = threading.Thread(target=dispose_leftover_food, args=(robots,))
task1_thread.start()
task2_thread.start()
task1_thread.join()
task2_thread.join()

task3_thread = threading.Thread(target=clean_cup, args=(robots,))
task4_thread = threading.Thread(target=dispose_trash, args=(robots,))
task3_thread.start()
task4_thread.start()
task3_thread.join()
task4_thread.join()

task5_thread = threading.Thread(target=clean_pan, args=(robots,))
task6_thread = threading.Thread(target=clean_pot, args=(robots,))
task5_thread.start()
task6_thread.start()
task5_thread.join()
task6_thread.join()

task7_thread = threading.Thread(target=clean_countertop, args=(robots,))
task8_thread = threading.Thread(target=dispose_garbage_bag, args=(robots,))
task7_thread.start()
task8_thread.start()
task7_thread.join()
task8_thread.join()

task9_thread = threading.Thread(target=clean_sink, args=(robots,))
task10_thread = threading.Thread(target=clean_garbagecan, args=(robots,))
task9_thread.start()
task10_thread.start()
task9_thread.join()
task10_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
