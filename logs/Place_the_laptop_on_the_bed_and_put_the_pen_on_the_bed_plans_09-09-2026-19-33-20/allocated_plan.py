# SOLUTION

## Analysis of Task Requirements:
1. **Place the laptop on the bed**:
   - Required skills: GoToObject, PickupObject, PutObject
   - Object mass: 2.3 kg (laptop)
   - Bed mass: 30 kg (but this is just the destination, not being moved)

2. **Put the pen on the bed**:
   - Required skills: GoToObject, PickupObject, PutObject
   - Object mass: 0.006 kg (pen)

## Robot Capabilities:
All robots have the required skills (GoToObject, PickupObject, PutObject), but differ in mass capacity:
- robot1: 5 kg capacity
- robot2: 0.4 kg capacity
- robot3: 0.08 kg capacity

## Optimal Allocation:
1. **Laptop Task**:
   - Only robot1 can handle the laptop (2.3 kg > robot2's 0.4 kg and robot3's 0.08 kg capacity)
   - Assign to robot1

2. **Pen Task**:
   - All robots can handle the pen (0.006 kg)
   - Since robot1 is busy with the laptop, assign to either robot2 or robot3
   - Both have sufficient capacity, so either can be chosen (I'll choose robot2)

## Parallel Execution:
- The two subtasks can be performed in parallel since they're independent
- robot1 handles the laptop while robot2 handles the pen simultaneously

## Final Allocation:
- **robot1**:
  - Subtask: Place the laptop on the bed
  - Action sequence:
    1. GoToObject(laptop)
    2. PickupObject(laptop)
    3. GoToObject(bed)
    4. PutObject(laptop, bed)

- **robot2**:
  - Subtask: Put the pen on the bed
  - Action sequence:
    1. GoToObject(pen)
    2. PickupObject(pen)
    3. GoToObject(bed)
    4. PutObject(pen, bed)

## Benefits:
- Minimum number of robots used (2 out of 3 available)
- Parallel execution reduces total task completion time
- All mass constraints are satisfied
- All skill requirements are met
- No need for robot teams as individual robots can handle each subtask