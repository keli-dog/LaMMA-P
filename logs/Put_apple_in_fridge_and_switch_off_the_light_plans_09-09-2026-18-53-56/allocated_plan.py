### SOLUTION

#### Analysis of Robots and Tasks:
1. **Robot Capabilities**: All three robots have identical skill sets and sufficient mass capacity (100 units) to handle all objects in the environment (max object mass is 85 units for DiningTable, which isn't involved in our tasks). The relevant skills for our tasks are:
   - SubTask 1 (Apple in Fridge): Requires GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   - SubTask 2 (Switch Off Light): Requires GoToObject, SwitchOff

2. **Parallelization Potential**: The two subtasks are completely independent (no shared objects or preconditions), allowing full parallel execution.

#### Optimal Allocation:
Since we have 3 identical robots and only 2 independent subtasks, we can assign:
- **Robot1**: Handle "Put Apple in Fridge" (SubTask 1)
- **Robot2**: Handle "Switch Off Light" (SubTask 2)
- **Robot3**: Remain idle (not needed for this task)

#### Justification:
1. **Skill Coverage**: Both assigned robots have all required skills for their respective tasks.
2. **Mass Capacity**: Apple (0.2 mass) and LightSwitch (0 mass) are well below robot capacity (100).
3. **Efficiency**: Parallel execution minimizes total task completion time.
4. **Redundancy**: Robot3 is available if either primary robot fails.

#### Execution Plan:
1. **Parallel Phase**:
   - Robot1 executes sequentially:
     - GoTo(Apple) → Pickup(Apple) → GoTo(Fridge) → Open(Fridge) → Put(Apple,Fridge) → Close(Fridge)
   - Robot2 executes:
     - GoTo(LightSwitch) → SwitchOff(LightSwitch)

2. **Completion**: Both tasks finish independently when their respective sequences complete.

This allocation satisfies all constraints while optimizing for:
- Minimal robots used (2/3)
- Full parallelization of independent tasks
- Skill and mass requirements met
- No resource conflicts between robots