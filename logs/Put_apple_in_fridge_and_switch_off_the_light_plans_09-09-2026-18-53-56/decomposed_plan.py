Here's the task decomposition for "Put apple in fridge and switch off the light":

### GENERAL TASK DECOMPOSITION
These subtasks can be parallelized since they don't depend on each other:
1. **SubTask 1**: Put an Apple in the Fridge (Skills: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
2. **SubTask 2**: Switch Off the Light (Skills: GoToObject, SwitchOff)

### ACTION SEQUENCE

#### Subtask 1: Put Apple in Fridge
1. **GoToObject**(robot1, Apple)
   - Pre: (not (inaction robot1))
   - Eff: (at robot1 Apple), clear other locations

2. **PickupObject**(robot1, Apple, CounterTop)
   - Pre: (at-location Apple CounterTop), (at robot1 CounterTop)
   - Eff: (holding robot1 Apple)

3. **GoToObject**(robot1, Fridge)
   - Pre: (not (inaction robot1))
   - Eff: (at robot1 Fridge)

4. **OpenFridge**(robot1, Fridge)
   - Pre: (at robot1 Fridge), (is-fridge Fridge)
   - Eff: (object-open robot1 Fridge), (increase (fridge-state Fridge) 1)

5. **PutObject**(robot1, Apple, Fridge)
   - Pre: (holding robot1 Apple), (at robot1 Fridge), (> (fridge-state Fridge) 0)
   - Eff: (at-location Apple Fridge), ¬(holding robot1 Apple)

6. **CloseFridge**(robot1, Fridge)
   - Pre: (at robot1 Fridge), (object-open robot1 Fridge)
   - Eff: (object-close robot1 Fridge), (decrease (fridge-state Fridge) 1)

#### Subtask 2: Switch Off Light (can run in parallel)
1. **GoToObject**(robot2, LightSwitch)
   - Pre: (not (inaction robot2))
   - Eff: (at robot2 LightSwitch)

2. **Switchoff**(robot2, LightSwitch)
   - Pre: (at robot2 LightSwitch)
   - Eff: (switch-off robot2 LightSwitch)

### PARALLELIZATION OPPORTUNITIES
- Robot1 can handle the fridge operations while Robot2 handles the light switch
- The only shared resource is robot availability (inaction predicate), but since we have multiple robots this isn't a constraint

### INITIAL CONDITIONS TO VERIFY
1. Apple is initially on CounterTop (at-location Apple CounterTop)
2. Fridge is initially closed (fridge-state Fridge = 0)
3. LightSwitch is initially on (need this as precondition though not explicitly modeled)
4. Robots start not in action (not (inaction robot1), not (inaction robot2))

This plan efficiently uses both robots to accomplish both tasks in minimal steps by parallelizing independent operations.