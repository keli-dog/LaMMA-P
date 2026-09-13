# TASK ALLOCATION

The two robots have identical skill sets, but different mass capacities:

- **robot1** mass capacity = **5 kg**
- **robot2** mass capacity = **0.02 kg**

Required object masses for the task include:

- Knife: 0.18 kg
- Apple: 0.2 kg
- Bread: 0.7 kg
- Lettuce: 0.47 kg
- Tomato: 0.12 kg
- Pot: 0.57 kg

Even the smallest required manipulable object, Tomato, is 0.12 kg, which exceeds robot2’s 0.02 kg capacity. Therefore, **robot2 cannot pick up or put down any required object** in this task.

## Subtask Allocation

### SubTask 1: Slice Apple, Bread, Lettuce, Tomato
- Skills required: `GoToObject`, `PickupObject` (Knife), `SliceObject`
- Both robots have these skills.
- However, robot1 must hold/carry the Knife (0.18 kg) and visit food items.
- robot2 cannot carry the Knife or any food item due to mass capacity 0.02 kg.
- **Robot1 should be assigned** to SubTask 1.

### SubTask 2: Clean the Pot
- Skills required: `GoToObject`, `CleanObject`
- **Neither robot1 nor robot2 has `CleanObject`** in its skill list.
- A team of robot1 + robot2 would still not have `CleanObject`.
- Also, cleaning would require handling the Pot (0.57 kg), which robot2 cannot carry.
- **This subtask cannot be performed with the available robots' skills.**  
  Therefore, the overall task as specified is infeasible unless `CleanObject` is available or the cleaning subtask is removed/revised.

### SubTask 3: Collect sliced items and put them into the cleaned Pot
- Depends on SubTask 1 and SubTask 2.
- Since SubTask 2 is infeasible, SubTask 3 cannot be validly scheduled.
- If SubTask 2 were possible, robot1 would be the only robot able to perform this because robot2 cannot carry the sliced food items or the Pot.

### SubTask 4: Archive Pot in Fridge
- Depends on SubTask 3.
- Requires `GoToObject`, `PickupObject`, `OpenObject`, `PutObject`, `CloseObject`.
- robot1 has all these skills and enough capacity to carry the loaded Pot (Pot + sliced food ≈ 2.06 kg, under 5 kg).
- robot2 cannot carry the Pot or its contents.
- **Robot1 would be the only feasible robot**, but it is blocked by SubTask 2 being impossible.

## Parallelization

- SubTask 1 and SubTask 2 are **independent** and could in principle be parallelized.
- However, no available robot has `CleanObject`, so SubTask 2 cannot be completed.
- SubTask 3 depends on both SubTask 1 and SubTask 2.
- SubTask 4 depends on SubTask 3.

## Conclusion

**No complete allocation satisfies all constraints** because the required `CleanObject` skill is not possessed by any robot or any possible robot team. If that skill requirement were waived, then **robot1 alone would perform all remaining object-handling subtasks sequentially**, and robot2 could not be used due to insufficient mass capacity.