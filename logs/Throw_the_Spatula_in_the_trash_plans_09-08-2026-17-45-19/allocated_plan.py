To allocate robots for the task of throwing the spatula in the trash, we need to analyze each subtask and ensure that the robots have the necessary skills to perform them. Here are the subtasks and their required skills:

1. **SubTask 1**: Go to the spatula.
   - **Skills Required**: GoToObject
2. **SubTask 2**: Pick up the spatula.
   - **Skills Required**: PickupObject
3. **SubTask 3**: Go to the trash.
   - **Skills Required**: GoToObject
4. **SubTask 4**: Throw the spatula in the trash.
   - **Skills Required**: ThrowObject

Given the robots and their skills:
- **Robot 1** has skills: `GoToObject`, `BreakObject`, `ThrowObject`
- **Robot 2** has skills: `GoToObject`, `PickupObject`, `PutObject`

### Task Allocation
1. **SubTask 1**: Go to the spatula.
   - Both robots have the required skill (`GoToObject`), so either robot can perform this task.

2. **SubTask 2**: Pick up the spatula.
   - Only Robot 2 has the required skill (`PickupObject`).

3. **SubTask 3**: Go to the trash.
   - Both robots have the required skill (`GoToObject`), so either robot can perform this task.

4. **SubTask 4**: Throw the spatula in the trash.
   - Only Robot 1 has the required skill (`ThrowObject`).

### Sequential Execution
Since SubTask 2 requires Robot 2 and SubTask 4 requires Robot 1, we need to ensure that these tasks are performed sequentially by their respective robots. Here is a possible sequence:

1. **Robot 2** performs SubTask 1: Go to the spatula.
2. **Robot 2** performs SubTask 2: Pick up the spatula.
3. **Robot 2** performs SubTask 3: Go to the trash.
4. **Robot 1** performs SubTask 4: Throw the spatula in the trash.

### Detailed Allocation
1. **SubTask 1**: Robot 2 goes to the spatula.
   - Action: GoToObject
   - Parameters: ?robot2, ?spatula

2. **SubTask 2**: Robot 2 picks up the spatula.
   - Action: PickupObject
   - Parameters: ?robot2, ?spatula, ?location

3. **SubTask 3**: Robot 2 goes to the trash.
   - Action: GoToObject
   - Parameters: ?robot2, ?trash

4. **SubTask 4**: Robot 1 throws the spatula in the trash.
   - Action: ThrowObject
   - Parameters: ?robot1, ?spatula

### Summary
- **Robot 2** will handle the first three subtasks (Go to the spatula, Pick up the spatula, Go to the trash).
- **Robot 1** will handle the final subtask (Throw the spatula in the trash).

This allocation ensures that each robot performs tasks for which they have the necessary skills and that tasks are performed sequentially as required.