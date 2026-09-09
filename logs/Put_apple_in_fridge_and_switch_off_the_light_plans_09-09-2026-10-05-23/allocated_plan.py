### SOLUTION

#### Analysis:
1. **Robot Capabilities**: All three robots (robot1, robot2, robot3) have identical skill sets and mass capacities (100 units). They all possess all required skills for both subtasks:
   - Skills for SubTask 1 (Put apple in fridge): GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   - Skills for SubTask 2 (Switch off light): GoToObject, SwitchOff

2. **Object Mass**: 
   - Apple mass: 0.2 (easily handled by any robot)
   - Fridge mass: 0 (static object, no lifting required)
   - LightSwitch mass: 0 (static object)

3. **Parallel Execution**: 
   - The two subtasks are completely independent and can be performed in parallel
   - No resource conflicts exist between the tasks

#### Optimal Allocation:
Since we have 3 identical robots available and only 2 independent subtasks, we can assign:
- **robot1**: Handle SubTask 1 (Put apple in fridge)
- **robot2**: Handle SubTask 2 (Switch off light)
- **robot3**: Remain idle (not needed for this task)

#### Justification:
1. **Minimum Robot Usage**: Using 2 robots meets the requirement of using the minimum number necessary
2. **Parallel Execution**: Both tasks can be completed simultaneously, reducing total execution time
3. **Skill Matching**: Both assigned robots have all required skills for their respective tasks
4. **Mass Capacity**: All objects involved have negligible mass compared to robot capacity (0.2 vs 100)
5. **No Team Required**: Each subtask can be completed by a single robot

#### Alternative Consideration:
If we wanted to complete the task even faster (though not necessary for this simple task), we could potentially break SubTask 1 into parallel components (e.g., one robot fetches apple while another opens fridge), but:
- The sequential steps within each subtask have natural dependencies
- The marginal time savings wouldn't justify using more robots
- The current solution is already optimal for the given task

#### Final Allocation:
```
SubTask 1 (Put apple in fridge): robot1
SubTask 2 (Switch off light): robot2
robot3: Unassigned (available for other tasks)
```