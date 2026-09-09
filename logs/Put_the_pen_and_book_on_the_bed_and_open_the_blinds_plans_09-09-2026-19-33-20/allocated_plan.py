### SOLUTION

#### Task Allocation Analysis:
1. **Subtask 1 (Put pen on bed)** and **Subtask 2 (Put book on bed)**:
   - Both require: GoToObject, PickupObject, PutObject
   - Can be performed in parallel
   - Mass considerations:
     - Pen mass: 0.006 (negligible)
     - Book mass: 0.5 (negligible)
     - Bed mass: 30 (but we're not moving the bed)

2. **Subtask 3 (Open blinds)**:
   - Requires: GoToObject, OpenObject
   - Must be performed separately
   - Blinds mass: 0 (negligible)

#### Robot Capabilities:
- **robot1**: Has all required skills for pen/book tasks (GoToObject, PickupObject, PutObject)
- **robot2**: Has all required skills for all tasks (including OpenObject)
- **robot4**: Has only basic skills for pen/book tasks (GoToObject, PickupObject, PutObject)

#### Optimal Allocation:
1. Assign **robot2** to **Subtask 3 (Open blinds)**:
   - Only robot with OpenObject skill
   - Can complete this independently while others work on other tasks

2. Assign **robot1** and **robot4** to **Subtask 1** and **Subtask 2** in parallel:
   - robot1: Put pen on bed
   - robot4: Put book on bed
   - Both have required skills and sufficient mass capacity

#### Execution Plan:
1. **Parallel Execution**:
   - robot2: Goes to blinds → Opens blinds
   - robot1: Goes to pen → Picks up pen → Goes to bed → Puts pen on bed
   - robot4: Goes to book → Picks up book → Goes to bed → Puts book on bed

2. **No Dependencies**:
   - All subtasks can run concurrently
   - No need for sequential execution

#### Why This Allocation Works:
- Uses minimum number of robots (3) to complete all tasks in parallel
- Matches robot skills exactly to task requirements
- All objects have negligible mass compared to robot capacity (100)
- No need for robot teams as all tasks can be done individually
- Maximizes parallelization potential

#### Alternative Considerations:
- If we wanted to use only 2 robots:
  - robot2 could do both opening blinds and one of the put tasks
  - But this would require sequential execution, increasing total time
- Current solution is optimal for time efficiency while respecting all constraints