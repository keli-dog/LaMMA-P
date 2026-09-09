# SOLUTION FOR "PUT MUG IN THE COFFEE MACHINE AND SWITCH ON THE COFFEE MACHINE"

# ANALYSIS OF ROBOT SKILLS:
# Robot2 has: ['GoToObject', 'PickupObject', 'PutObject'] - Can perform SubTask1
# Robot3 has: ['GoToObject', 'SwitchOn', 'SwitchOff'] - Can perform SubTask2
# The third robot (also named robot3) has irrelevant skills for this task

# MASS ANALYSIS:
# Mug mass: 1.0 (well below all robots' capacity of 100)
# CoffeeMachine mass: 5.0 (well below all robots' capacity of 100)
# No mass constraints prevent any robot from performing the tasks

# TASK ALLOCATION:
# Since the subtasks must be performed sequentially:
# 1. Assign SubTask1 (Put mug in coffee machine) to robot2
#   - robot2 has all required skills (GoToObject, PickupObject, PutObject)
#   - robot2 has sufficient mass capacity
# 2. After SubTask1 is complete, assign SubTask2 (Switch on coffee machine) to robot3
#   - robot3 has all required skills (GoToObject, SwitchOn)
#   - robot3 has sufficient mass capacity

# EXECUTION PLAN:
1. robot2 performs:
   - GoToObject(Mug)
   - PickupObject(Mug)
   - GoToObject(CoffeeMachine)
   - PutObject(Mug, CoffeeMachine)
2. After robot2 completes, robot3 performs:
   - GoToObject(CoffeeMachine)
   - SwitchOn(CoffeeMachine)

# No teams required since each subtask can be performed by individual robots
# Minimum number of robots used (2) - one for each sequential subtask
# All skill and mass constraints are satisfied