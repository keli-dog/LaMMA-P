# Task Description: Throw the Spatula in the trash

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible.
# This task is a single linear sequence — no parallelization needed.
# SubTask 1: Dispose of the Spatula in the GarbageCan. (Skills Required: GoToObject, PickupObject, PutObject)

# Action descriptions from domain for tasks required

# SubTask 1: Throw the Spatula in the GarbageCan

# Initial condition analyze:
# 1. Robot not at Spatula location.
# 2. Robot not holding Spatula.
# 3. GarbageCan is at a fixed location (mass 0.0 → stationary).

GoToObject: Robot goes to the Spatula.
Parameters: ?robot, ?Spatula
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?Spatula), (not (inaction ?robot))

PickupObject: Robot picks up the Spatula.
Parameters: ?robot,