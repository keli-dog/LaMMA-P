# Task Decomposition: Put plunger in cabinet and Turn off the light

## Analysis of Task Requirements
This task has two independent components that can be performed in parallel:
1. Putting the plunger in the cabinet
2. Turning off the light

## Available Robots
From the given robots:
- robot2: Can perform GoToObject, SwitchOn, SwitchOff (suitable for turning off light)
- robot3: Can perform GoToObject, PickupObject, PutObject (suitable for handling plunger)

## Parallel Subtasks

### Subtask 1: Put plunger in cabinet (robot3)
#### Initial Conditions:
1. Robot not holding plunger
2. Plunger is at initial location
3. Cabinet is closed (default state)

#### Action Sequence:
1. GoToObject(robot3, Plunger)
   - Pre: not (inaction robot3)
   - Eff: at robot3 Plunger, not (inaction robot3)

2. PickupObject(robot3, Plunger, PlungerLocation)
   - Pre: at-location Plunger PlungerLocation, at robot3 PlungerLocation, not (inaction robot3)
   - Eff: holding robot3 Plunger, not (inaction robot3)

3. GoToObject(robot3, Cabinet)
   - Pre: not (inaction robot3)
   - Eff: at robot3 Cabinet, not (inaction robot3)

4. OpenObject(robot3, Cabinet)
   - Pre: not (inaction robot3), at robot3 Cabinet
   - Eff: object-open robot3 Cabinet, not (inaction robot3)

5. PutObject(robot3, Plunger, Cabinet)
   - Pre: holding robot3 Plunger, at robot3 Cabinet, not (inaction robot3)
   - Eff: at-location Plunger Cabinet, not (holding robot3 Plunger), not (inaction robot3)

6. CloseObject(robot3, Cabinet)
   - Pre: not (inaction robot3), at robot3 Cabinet
   - Eff: object-close robot3 Cabinet, not (inaction robot3)

### Subtask 2: Turn off the light (robot2)
#### Initial Conditions:
1. Light is initially on (assuming)
2. Robot not at light switch

#### Action Sequence:
1. GoToObject(robot2, LightSwitch)
   - Pre: not (inaction robot2)
   - Eff: at robot2 LightSwitch, not (inaction robot2)

2. SwitchOff(robot2, LightSwitch)
   - Pre: not (inaction robot2), at robot2 LightSwitch
   - Eff: switch-off robot2 LightSwitch, not (inaction robot2)

## Parallel Execution Plan
These two subtasks can be executed simultaneously by robot2 and robot3 since:
1. They use different robots
2. They manipulate different objects (plunger/cabinet vs light switch)
3. There are no dependencies between the tasks

## Final State Verification
After both subtasks complete:
1. Plunger should be inside the closed cabinet
2. Light should be switched off
3. Both robots should be free (not in action)