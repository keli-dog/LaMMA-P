#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: prepare_hot_water_for_shower_and_put_toilet_paper_in_the_trash_plans_09-09-2026-20-50-22
Scene ID: pddl_generated
Task: prepare hot water for shower and put toilet paper in the trash
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def prepare_hot_water(robots):
    GoToObject(robots[0], 'Faucet')
    SwitchOn(robots[0], 'Faucet')
    GoToObject(robots[0], 'Bathtub')
    SwitchOff(robots[0], 'Faucet')

def dispose_toiletpaper(robots):
    GoToObject(robots[1], 'ToiletPaper')
    PickupObject(robots[1], 'ToiletPaper')
    GoToObject(robots[1], 'GarbageCan')
    PutObject(robots[1], 'ToiletPaper', 'GarbageCan')

task1_thread = threading.Thread(target=prepare_hot_water, args=(robots,))
task2_thread = threading.Thread(target=dispose_toiletpaper, args=(robots,))

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
