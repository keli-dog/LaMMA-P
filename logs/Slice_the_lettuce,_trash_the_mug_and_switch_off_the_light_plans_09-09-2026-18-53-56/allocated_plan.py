### SOLUTION

#### Analysis of Subtasks and Robot Capabilities:
1. **SubTask 1: Slice the Lettuce**
   - Required Skills: GoToObject, PickupObject, SliceObject
   - Object Masses: Knife (0.18), Lettuce (0.47)
   - Total mass to handle: 0.65 (but only one object held at a time)
   - Robot Requirements:
     - Must have all 3 skills
     - Mass capacity ≥ 0.47 (lettuce is heavier than knife)

2. **SubTask 2: Trash the Mug**
   - Required Skills: GoToObject, PickupObject, PutObject
   - Object Mass: Mug (1.0)
   - Robot Requirements:
     - Must have all 3 skills
     - Mass capacity ≥ 1.0

3. **SubTask 3: Switch Off the Light**
   - Required Skills: GoToObject, SwitchOff
   - Object Mass: LightSwitch (0.0)
   - Robot Requirements:
     - Must have both skills
     - No mass constraints

#### Robot Skill Analysis:
All robots have the complete skill set required for all subtasks:
['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject']

#### Mass Capacity Constraints:
- robot1: 0.4 (cannot handle lettuce or mug)
- robot2: 2.1 (can handle all objects)
- robot3: 1.0 (can handle lettuce and mug, but not both simultaneously)

#### Optimal Allocation:
1. **robot2 (2.1 capacity)**:
   - Assign the most mass-intensive task: **Trash the Mug (1.0 mass)**
   - This leaves robot3 free for other tasks

2. **robot3 (1.0 capacity)**:
   - Assign **Slice the Lettuce** (max mass 0.47)
   - Can handle both knife (0.18) and lettuce (0.47) separately

3. **robot1 (0.4 capacity)**:
   - Only suitable for **Switch Off the Light** (0 mass)
   - All other tasks exceed its capacity

#### Parallel Execution Plan:
All three subtasks can be performed in parallel by:
- robot2: Trash the Mug
- robot3: Slice the Lettuce
- robot1: Switch Off the Light

#### Alternative if robot1 is unavailable:
robot3 could sequentially:
1. First do Switch Off the Light (fastest task)
2. Then do Slice the Lettuce
While robot2 handles Trash the Mug

But with all robots available, the parallel allocation is optimal.

### Final Allocation:
- **robot1**: Switch Off the Light
- **robot2**: Trash the Mug
- **robot3**: Slice the Lettuce

All tasks can be completed in parallel with this allocation, satisfying all skill and mass constraints.