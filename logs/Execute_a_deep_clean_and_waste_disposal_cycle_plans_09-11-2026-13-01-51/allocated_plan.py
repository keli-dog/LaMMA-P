# SOLUTION

- Robot skills are identical across all three robots, but **no robot has the `CleanObject` skill** required for SubTask 1. Therefore, SubTask 1 cannot be assigned to any individual robot or team.

- SubTask 2 requires `GoToObject`, `PickupObject`, and `PutObject`.  
  All robots possess these skills, so the skill requirement is satisfied.

- However, the waste item to dispose of is the **GarbageBag**, with mass ≈ `3.5`.  
  Individual mass capacities:
  - robot1: `0.4`
  - robot2: `2.1`
  - robot3: `1.0`

  No single robot can handle the GarbageBag.  
  Combined mass capacity:
  - robot1 + robot2 + robot3 = `0.4 + 2.1 + 1.0 = 3.5`

  This is just enough to handle the GarbageBag mass of `3.499999761581421`.

### Task Allocation

- **SubTask 1: Clean all dirty items and surfaces**  
  **Not assignable** — missing required skill `CleanObject`.

- **SubTask 2: Dispose of waste and garbage**  
  **Assign to robot team: `{robot1, robot2, robot3}`**  
  Since no smaller team has enough combined mass capacity, all three robots are necessary.  
  The team will collectively:
  1. `GoToObject` to the GarbageBag  
  2. `PickupObject` the GarbageBag  
  3. `GoToObject` to the GarbageCan  
  4. `PutObject` the GarbageBag in the GarbageCan  

Because SubTask 1 cannot be executed, only SubTask 2 is allocated. The two subtasks cannot be parallelized in practice because the only feasible subtask requires all available robots.