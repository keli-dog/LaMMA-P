### SOLUTION

#### Task Analysis:
The task "Parallelly put pen and book on the bed" consists of two independent subtasks that can be executed in parallel:
1. **SubTask 1**: Put the pen on the bed (Skills: GoToObject, PickupObject, PutObject)
2. **SubTask 2**: Put the book on the bed (Skills: GoToObject, PickupObject, PutObject)

#### Robot Skills Analysis:
- **robot1**: Has all required skills (GoToObject, PickupObject, PutObject)
- **robot2**: Has all required skills (GoToObject, PickupObject, PutObject)
- **robot4**: Has all required skills (GoToObject, PickupObject, PutObject)

#### Mass Capacity Check:
All objects involved are lightweight:
- Pen: 0.006 mass units
- Book: 0.5 mass units
- Bed: 30 mass units (destination, not carried)
All robots have mass capacity of 100, which is sufficient.

#### Optimal Allocation:
Since we have 3 robots available but only 2 parallel subtasks, we can assign:
- **SubTask 1 (Pen)**: Assign to robot1
- **SubTask 2 (Book)**: Assign to robot2
- **robot4**: Will remain idle (no need to use all robots when minimum sufficient are available)

#### Parallel Execution Plan:
```
Time | robot1 Actions            | robot2 Actions
-----|---------------------------|---------------------------
T1   | GoToObject(robot1, pen)   | GoToObject(robot2, book)
T2   | PickupObject(robot1, pen) | PickupObject(robot2, book)
T3   | GoToObject(robot1, bed)   | GoToObject(robot2, bed)
T4   | PutObject(robot1, pen)    | PutObject(robot2, book)
```

#### Why This Allocation:
1. **Skills Match**: Both assigned robots have all required skills
2. **Mass Capacity**: All objects are well within capacity
3. **Parallelism**: Tasks are truly independent and can run simultaneously
4. **Efficiency**: Uses minimum necessary robots (2 out of 3 available)
5. **No Conflicts**: Different robots handling different objects prevents any resource contention

#### Alternative Considerations:
- We could have used robot4 instead of robot1 or robot2, but since all have equal capability, the choice is arbitrary
- Using robot4 might be preferable if robot1/robot2 had higher-level skills needed for other tasks
- No need for robot teams since all subtasks can be handled by individual robots

This allocation satisfies all constraints while maximizing parallel execution efficiency.