#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Organize_personal_inventory_and_garden_tools_plans_09-09-2026-20-47-40
Scene ID: pddl_generated
Task: Organize personal inventory and garden tools
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def organize_heavy_objects(robots):
    GoToObject(robots[0], 'ArmChair')
    PickupObject(robots[0], 'ArmChair')
    GoToObject(robots[0], 'Dresser')
    PutObject(robots[0], 'ArmChair', 'Dresser')
    GoToObject(robots[0], 'Sofa')
    PickupObject(robots[0], 'Sofa')
    GoToObject(robots[0], 'Dresser')
    PutObject(robots[0], 'Sofa', 'Dresser')
    GoToObject(robots[0], 'CoffeeTable')
    PickupObject(robots[0], 'CoffeeTable')
    GoToObject(robots[0], 'SideTable')
    PutObject(robots[0], 'CoffeeTable', 'SideTable')

def organize_small_objects(robots):
    GoToObject(robots[1], 'Book')
    PickupObject(robots[1], 'Book')
    GoToObject(robots[1], 'Shelf')
    PutObject(robots[1], 'Book', 'Shelf')
    GoToObject(robots[1], 'Laptop')
    PickupObject(robots[1], 'Laptop')
    GoToObject(robots[1], 'Shelf')
    PutObject(robots[1], 'Laptop', 'Shelf')
    GoToObject(robots[1], 'Vase')
    PickupObject(robots[1], 'Vase')
    GoToObject(robots[1], 'Shelf')
    PutObject(robots[1], 'Vase', 'Shelf')
    GoToObject(robots[1], 'RemoteControl')
    PickupObject(robots[1], 'RemoteControl')
    GoToObject(robots[1], 'Drawer')
    PutObject(robots[1], 'RemoteControl', 'Drawer')

task1_thread = threading.Thread(target=organize_heavy_objects, args=(robots,))
task2_thread = threading.Thread(target=organize_small_objects, args=(robots,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

action_queue.append({'action':'Done'})
action_queue.append({'action':'Done'})

task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
