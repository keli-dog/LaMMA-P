# Task Allocation Solution for "Put plunger in cabinet and Turn off the light"

## Analysis
The task consists of two independent subtasks that can be performed in parallel:
1. Put plunger in cabinet
2. Turn off the light

## Robot Capabilities
- robot2: Has skills ['GoToObject', 'SwitchOn', 'SwitchOff'] (ideal for turning off light)
- robot3: Has skills ['GoToObject', 'PickupObject', 'PutObject'] (ideal for handling plunger)

## Mass Considerations
All objects have mass ≤ 1.0, and both robots have mass capacity of 100, so mass is not a limiting factor.

## Optimal Allocation
1. **Subtask 1: Put plunger in cabinet**
   - Assigned to robot3 (has all required skills: GoToObject, PickupObject, PutObject)
   - Action sequence:
     a. GoToObject(plunger)
     b. PickupObject(plunger)
     c. GoToObject(cabinet)
     d. OpenObject(cabinet) [assuming robot3 can open objects]
     e. PutObject(plunger, cabinet)
     f. CloseObject(cabinet)

2. **Subtask 2: Turn off the light**
   - Assigned to robot2 (has all required skills: GoToObject, SwitchOff)
   - Action sequence:
     a. GoToObject(light switch)
     b. SwitchOff(light switch)

## Parallel Execution
Both subtasks can be executed simultaneously since:
- They use different robots
- They manipulate different objects
- There are no dependencies between them

## Potential Issues
- robot3 may need OpenObject/CloseObject skills which aren't listed (assuming it can perform these basic operations)
- If cabinet is initially open, OpenObject steps can be skipped

## Final Allocation
- robot3: Handles plunger task (putting in cabinet)
- robot2: Handles light task (turning off light)

This allocation:
- Uses minimum number of robots (2)
- Matches skills to tasks perfectly
- Allows parallel execution
- Handles all mass requirements
- Completes both tasks efficiently