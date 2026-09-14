#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Wash_the_fork_and_put_it_in_the_bowl,_and_turn_off_the_light_plans_09-09-2026-19-08-31
Scene ID: pddl_generated
Task: Wash the fork and put it in the bowl, and turn off the light
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def wash_fork_put_in_bowl(robots):
    GoToObject(robots[0], 'Fork')
    PickupObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Sink')
    CleanObject(robots[0], 'Fork')
    GoToObject(robots[0], 'Bowl')
    PutObject(robots[0], 'Fork', 'Bowl')

def turn_off_light(robots):
    GoToObject(robots[1], 'LightSwitch')
    SwitchOff(robots[1], 'LightSwitch')

task1_thread = threading.Thread(target=wash_fork_put_in_bowl, args=(robots,))
task2_thread = threading.Thread(target=turn_off_light, args=(robots,))

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
