#!/usr/bin/env python3
"""
Plan-to-Code Format for AI2-THOR Controller
Generated from Complete PDDL Plan Translation

Episode ID: Secure_the_kitchen_for_the_night_plans_09-11-2026-13-01-51
Scene ID: pddl_generated
Task: Secure the kitchen for the night
Validation Passed: True
Validation Message: Validation skipped
"""

import time
import threading

# Import AI2-THOR controller functions
# from ai2thor_controller import GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff

def secure_kitchen(robots):
    GoToObject(robots[0], 'CoffeeMachine')
    GoToObject(robots[1], 'Blinds')
    GoToObject(robots[2], 'Fridge')
    SwitchOff(robots[0], 'CoffeeMachine')
    CloseObject(robots[1], 'Blinds')
    CloseObject(robots[2], 'Fridge')
    GoToObject(robots[0], 'LightSwitch')
    GoToObject(robots[1], 'Cabinet')
    SwitchOff(robots[0], 'LightSwitch')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[0], 'Microwave')
    GoToObject(robots[1], 'Cabinet')
    SwitchOff(robots[0], 'Microwave')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[0], 'StoveKnob')
    GoToObject(robots[1], 'Cabinet')
    SwitchOff(robots[0], 'StoveKnob')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[0], 'StoveKnob')
    GoToObject(robots[1], 'Cabinet')
    SwitchOff(robots[0], 'StoveKnob')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[0], 'StoveKnob')
    GoToObject(robots[1], 'Cabinet')
    SwitchOff(robots[0], 'StoveKnob')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[0], 'StoveKnob')
    GoToObject(robots[1], 'Cabinet')
    SwitchOff(robots[0], 'StoveKnob')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[0], 'Toaster')
    GoToObject(robots[1], 'Cabinet')
    SwitchOff(robots[0], 'Toaster')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[1], 'Cabinet')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[1], 'Cabinet')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[1], 'Cabinet')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[1], 'Cabinet')
    CloseObject(robots[1], 'Cabinet')
    GoToObject(robots[1], 'Drawer')
    CloseObject(robots[1], 'Drawer')
    GoToObject(robots[1], 'Drawer')
    CloseObject(robots[1], 'Drawer')
    GoToObject(robots[1], 'Drawer')
    CloseObject(robots[1], 'Drawer')
    GoToObject(robots[1], 'Window')
    CloseObject(robots[1], 'Window')

task1_thread = threading.Thread(target=secure_kitchen, args=(robots,))
task1_thread.start()
task1_thread.join()
action_queue.append({'action':'Done'})
task_over = True
time.sleep(5)

# Example usage:
# robot = get_robot_instance()
# execute_task(robot)
