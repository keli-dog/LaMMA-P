Here's the task decomposition for "Put apple in fridge and switch off the light" with parallelizable subtasks:

### GENERAL TASK DECOMPOSITION
We can identify two independent subtasks that can be performed in parallel by different robots:
1. **SubTask 1**: Put an apple in the fridge
2. **SubTask 2**: Switch off the light

### SUBTASK 1: Put an Apple in the Fridge
**Skills Required**: GoToObject, PickupObject, OpenObject, PutObject, CloseObject

#### Action Sequence:
1. **GoToObject**(robot1, Apple)
   - Pre: (not (inaction robot1))
   - Eff: (at robot1 Apple), clear other locations

2. **PickupObject**(robot1, Apple, AppleLocation)
   - Pre: (at-location Apple AppleLocation), (at robot1 AppleLocation)
   - Eff: (holding robot1 Apple)

3. **GoToObject**(robot1, Fridge)
   - Pre: (not (inaction robot1))
   - Eff: (at robot1 Fridge)

4. **OpenObject**(robot1, Fridge)
   - Pre: (at robot1 Fridge), (is-fridge Fridge)
   - Eff: (object-open robot1 Fridge), (increase (fridge-state Fridge) 1)

5. **PutObject**(robot1, Apple, Fridge)
   - Pre: (holding robot1 Apple), (at robot1 Fridge), (> (fridge-state Fridge) 0)
   - Eff: (at-location Apple Fridge), (not (holding robot1 Apple))

6. **CloseObject**(robot1, Fridge)
   - Pre: (at robot1 Fridge), (object-open robot1 Fridge)
   - Eff: (object-close robot1 Fridge), (decrease (fridge-state Fridge) 1)

### SUBTASK 2: Switch Off the Light
**Skills Required**: GoToObject, SwitchOff

#### Action Sequence:
1. **GoToObject**(robot2, LightSwitch)
   - Pre: (not (inaction robot2))
   - Eff: (at robot2 LightSwitch)

2. **SwitchOff**(robot2, LightSwitch)
   - Pre: (at robot2 LightSwitch)
   - Eff: (switch-off robot2 LightSwitch)

### PARALLEL EXECUTION NOTES:
- These subtasks can be performed simultaneously by different robots since:
  - They don't share any resources that would cause conflicts
  - They don't have any ordering dependencies
  - They don't affect each other's preconditions

### INITIAL CONDITIONS ASSUMPTIONS:
1. Apple is initially at some location (AppleLocation)
2. Fridge is initially closed (fridge-state = 0)
3. Light is initially on (switch-on state)
4. Robots are not holding any objects initially
5. Robots are not in action initially

### FINAL CONDITIONS:
1. Apple is inside the fridge
2. Fridge door is closed
3. Light is switched off

This decomposition allows for efficient parallel execution while ensuring all task requirements are met. The two subtasks can be assigned to different robots to minimize total execution time.