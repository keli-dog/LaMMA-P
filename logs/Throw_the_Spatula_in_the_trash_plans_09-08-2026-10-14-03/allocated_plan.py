To solve this task allocation problem for throwing a spatula into the trash using two available robots with specific skill sets and mass capacities, we need to break down the required actions and match them against each robot's capabilities.

### Task Decomposition

1. **SubTask 1: Go to Spatula**
   - Action: `GoToObject`
     - Parameters: ?robot, spatula
     - Skills Required: `GoToObject`

2. **SubTask 2: Pick up Spatula**
   - Action: `PickupObject`
     - Parameters: ?robot, spatula
     - Skills Required: `PickupObject`

3. **SubTask 3: Go to Garbage Can**
   - Action: `GoToObject`
     - Parameters: ?robot, garbageCan
     - Skills Required: `GoToObject`

4. **SubTask 4: Throw Spatula into Garbage Can**
   - Action: `ThrowObject`
     - Parameters: ?robot, spatula
     - Skills Required: `ThrowObject`

### Robot Capabilities

- **Robot1**: 
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 (sufficient for all objects)

- **Robot2**:
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 (sufficient for all objects)

### Task Allocation

Given the task decomposition and robot capabilities:

- SubTask 1 (`GoToObject` to spatula) can be performed by both robots.
- SubTask 2 (`PickupObject`) requires `PickupObject`, which only Robot2 has.
- SubTask 3 (`GoToObject` to garbageCan) can be performed by both robots.
- SubTask 4 (`ThrowObject`) requires `ThrowObject`, which only Robot1 has.

Since the subtasks are sequential and dependent on each other, we need a single robot that can perform all required actions. However, no individual robot possesses all necessary skills (both PickupObject and ThrowObject). Therefore, we must form a team of robots to complete this task:

- **Robot2** will handle `GoToObject` to spatula and `PickupObject`.
- After Robot2 picks up the spatula, it can hand over the spatula to **Robot1**, who then performs `GoToObject` to garbageCan and finally `ThrowObject`.

### Detailed Allocation

1. **SubTask 1: Go to Spatula**
   - Assigned to: Robot2
     - Action: `GoToObject`
   
2. **SubTask 2: Pick up Spatula**
   - Assigned to: Robot2
     - Action: `PickupObject`

3. **Handover Task**:
   - Hand over spatula from Robot2 to Robot1 (this is an implicit step and not explicitly defined in the action set, but necessary for task completion).

4. **SubTask 3: Go to Garbage Can**
   - Assigned to: Robot1
     - Action: `GoToObject`

5. **SubTask 4: Throw Spatula into Garbage Can**
   - Assigned to: Robot1
     - Action: `ThrowObject`

### Summary

- **Robot2** will go to the spatula and pick it up.
- After picking up, Robot2 hands over the spatula to **Robot1**, who then goes to the garbage can and throws the spatula into it.

This ensures that all necessary skills are utilized effectively by both robots in a sequential manner.