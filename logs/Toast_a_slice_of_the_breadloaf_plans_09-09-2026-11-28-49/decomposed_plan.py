# Task Decomposition: Toast a slice of the breadloaf

## GENERAL TASK DECOMPOSITION
This task can be broken down into the following subtasks:

1. **Prepare Bread Slice**: Get a slice of bread ready for toasting
2. **Operate Toaster**: Place bread in toaster and activate it
3. **Retrieve Toast**: Get the toasted bread from the toaster

## Required Skills:
- GoToObject
- PickupObject
- PutObject
- SwitchOn
- SwitchOff

## Parallelization Opportunities:
This is a linear task with dependencies between steps, so parallelization isn't possible.

## Action Sequence:

### Subtask 1: Prepare Bread Slice
Initial conditions:
1. Robot not holding bread
2. Robot not at bread location
3. Robot not holding knife

```
GoToObject(robot, Knife)
Parameters: ?robot - robot, ?Knife - object
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?Knife), (not (inaction ?robot))

PickupObject(robot, Knife, KnifeLocation)
Parameters: ?robot - robot, ?Knife - object, ?KnifeLocation - object
Preconditions: (at-location ?Knife ?KnifeLocation), (at ?robot ?KnifeLocation), (not (inaction ?robot))
Effects: (holding ?robot ?Knife), (not (inaction ?robot))

GoToObject(robot, Bread)
Parameters: ?robot - robot, ?Bread - object
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?Bread), (not (inaction ?robot))

SliceObject(robot, Bread)
Parameters: ?robot - robot, ?Bread - object
Preconditions: (holding ?robot ?Knife), (at ?robot ?Bread), (not (inaction ?robot))
Effects: (sliced ?Bread), (not (inaction ?robot))
```

### Subtask 2: Operate Toaster
Initial conditions:
1. Bread is sliced
2. Robot is holding bread slice
3. Toaster is off

```
GoToObject(robot, Toaster)
Parameters: ?robot - robot, ?Toaster - object
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?Toaster), (not (inaction ?robot))

PutObject(robot, BreadSlice, Toaster)
Parameters: ?robot - robot, ?BreadSlice - object, ?Toaster - object
Preconditions: (holding ?robot ?BreadSlice), (at ?robot ?Toaster), (not (inaction ?robot))
Effects: (at-location ?BreadSlice ?Toaster), (not (holding ?robot ?BreadSlice)), (not (inaction ?robot))

SwitchOn(robot, Toaster)
Parameters: ?robot - robot, ?Toaster - object
Preconditions: (at ?robot ?Toaster), (not (inaction ?robot))
Effects: (switch-on ?robot ?Toaster), (not (inaction ?robot))

[Wait for toasting to complete]

SwitchOff(robot, Toaster)
Parameters: ?robot - robot, ?Toaster - object
Preconditions: (at ?robot ?Toaster), (switch-on ?robot ?Toaster), (not (inaction ?robot))
Effects: (switch-off ?robot ?Toaster), (not (inaction ?robot))
```

### Subtask 3: Retrieve Toast
Initial conditions:
1. Toast is in toaster
2. Toaster is off

```
PickupObject(robot, Toast, Toaster)
Parameters: ?robot - robot, ?Toast - object, ?Toaster - object
Preconditions: (at-location ?Toast ?Toaster), (at ?robot ?Toaster), (not (inaction ?robot))
Effects: (holding ?robot ?Toast), (not (inaction ?robot))

GoToObject(robot, Plate)
Parameters: ?robot - robot, ?Plate - object
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?Plate), (not (inaction ?robot))

PutObject(robot, Toast, Plate)
Parameters: ?robot - robot, ?Toast - object, ?Plate - object
Preconditions: (holding ?robot ?Toast), (at ?robot ?Plate), (not (inaction ?robot))
Effects: (at-location ?Toast ?Plate), (not (holding ?robot ?Toast)), (not (inaction ?robot))
```

## Notes:
1. The "Wait for toasting to complete" step would need to be handled by either:
   - A timer