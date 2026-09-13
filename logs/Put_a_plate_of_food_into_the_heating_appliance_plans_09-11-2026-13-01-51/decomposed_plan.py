# GENERAL TASK DECOMPOSITION 
Decompose and parallel subtasks where ever possible.

# Task Description: Put a plate of food into the heating appliance.

# Independent subtasks:
# SubTask 1: Acquire the plate of food. (Skills Required: GoToObject, PickupObject)
# SubTask 2: Prepare the heating appliance. (Skills Required: GoToObject, OpenObject)
# SubTask 3: Place the plate into the appliance and close it. (Skills Required: GoToObject, PutObject, CloseObject)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

---

#Subtask 1: Acquire the plate of food

# Initial condition analyze due to previous subtask:
# 1. Robot not at plate location.
# 2. Robot not holding plate.

GoToObject: Robot goes to the plate.
Parameters: ?robot, ?plate
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?plate), (not (inaction ?robot))

PickupObject: Robot picks up the plate.
Parameters: ?robot, ?plate, ?location (where plate is initially located)
Preconditions: (at-location ?plate ?location), (at ?robot ?location), (not (inaction ?robot))
Effects: (holding ?robot ?plate), (not (inaction ?robot))

---

#Subtask 2: Prepare the heating appliance

# Initial condition analyze due to previous subtask:
# 1. Robot not at appliance location.
# 2. Appliance is initially closed.

GoToObject: Robot goes to the heating appliance.
Parameters: ?robot, ?appliance
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?appliance), (not (inaction ?robot))

OpenObject: Robot opens the heating appliance.
Parameters: ?robot, ?appliance
Preconditions: (at ?robot ?appliance), (not (inaction ?robot))
Effects: (object-open ?robot ?appliance), (not (inaction ?robot))

---

#Subtask 3: Place the plate into the appliance and close it

# Initial condition due to previous subtasks:
# 1. Robot holds the plate (from SubTask 1).
# 2. Appliance is open (from SubTask 2).
# 3. Robot may not be at the appliance yet (if SubTask 1 and 2 were done by different robots, or the same robot moved away after picking the plate).

GoToObject: Robot goes to the heating appliance (if not already there).
Parameters: ?robot, ?appliance
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?appliance), (not (inaction ?robot))

PutObject: Robot places the plate inside the appliance.
Parameters: ?robot, ?plate, ?appliance
Preconditions: (holding ?robot ?plate), (at ?robot ?appliance), (not (inaction ?robot))
Effects: (at-location ?plate ?appliance), (not (holding ?robot ?plate)), (not (inaction ?robot))

CloseObject: Robot closes the appliance.
Parameters: ?robot, ?appliance
Preconditions: (at ?robot ?appliance), (not (inaction ?robot))
Effects: (object-close ?robot ?appliance), (not (inaction ?robot))

# Task Put a plate of food into the heating appliance is done.