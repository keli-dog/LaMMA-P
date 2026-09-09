### SOLUTION

#### Analysis of Robots and Tasks:
1. **Robot Capabilities**: All three robots (robot1, robot2, robot3) have identical skill sets and mass capacities (100 units). They can perform all required actions (GoToObject, PickupObject, PutObject, SwitchOff, etc.).
2. **Object Masses**: 
   - BaseballBat: 0.9 units
   - TennisRacket: 0.31 units
   - Bed: 29.99 units (destination, not carried)
   - LightSwitch: 0 units
   All objects are well within the mass capacity of any robot.

#### Task Allocation:
Since we have three independent subtasks and three robots with identical capabilities, we can assign each subtask to a separate robot for maximum parallelization:

1. **SubTask 1 (BaseballBat on Bed)**:
   - Assign to: robot1
   - Skills needed: GoToObject, PickupObject, PutObject
   - Mass constraints: BaseballBat (0.9) << 100 (robot capacity)

2. **SubTask 2 (TennisRacket on Bed)**:
   - Assign to: robot2
   - Skills needed: GoToObject, PickupObject, PutObject
   - Mass constraints: TennisRacket (0.31) << 100 (robot capacity)

3. **SubTask 3 (Turn off Light)**:
   - Assign to: robot3
   - Skills needed: GoToObject, SwitchOff
   - Mass constraints: LightSwitch (0) << 100 (robot capacity)

#### Execution Plan:
All three subtasks can be executed in parallel since:
- They are independent (no shared resources or dependencies)
- Each robot has all required skills
- No object exceeds robot mass capacity

#### Final Allocation:
- robot1: BaseballBat → Bed
- robot2: TennisRacket → Bed
- robot3: Turn off Light

This solution:
- Uses all available robots efficiently
- Completes the task in minimal time (parallel execution)
- Satisfies all skill and mass constraints
- No need for robot teams (single robots suffice for each subtask)