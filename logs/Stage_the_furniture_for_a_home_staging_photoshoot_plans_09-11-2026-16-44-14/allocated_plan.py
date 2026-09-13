SOLUTION

**Feasibility check:**

- **SubTask 1 – Clean all furniture surfaces** requires the skill `CleanObject`.  
  Neither `robot1` nor `robot2` has `CleanObject` in its skill list. A team cannot supply a skill that neither robot possesses.  
  **Therefore SubTask 1 cannot be assigned to any robot or team.** Since cleaning is a required part of the staging task, the full task is **infeasible with the provided robots.**

- **SubTask 2 – Turn on lights** requires `GoToObject` and `SwitchOn`.  
  Both robots have these skills. No heavy object needs to be lifted; the FloorLamp is only switched on, not moved, so mass capacity is not an issue.

- **SubTask 3 – Place decorative items** requires `GoToObject`, `PickupObject`, and `PutObject`.  
  Both robots have these skills, but:
  - `robot1` capacity = 0.4 kg, so it **cannot** carry the `Book` (0.5 kg).
  - `robot2` capacity = 0.9 kg, so it can carry every decorative item if handled one at a time.

**Best feasible partial allocation:**

- **Minimum robot count:** `robot2` alone can perform all feasible tasks, because it has all required skills and enough capacity.
- **SubTask 2:** assign to `robot2`
  - `GoToObject FloorLamp` → `SwitchOn FloorLamp`
  - `GoToObject LightSwitch` → `SwitchOn LightSwitch`
- **SubTask 3:** assign to `robot2`
  - For each item: `GoToObject item` → `PickupObject item` → `GoToObject target surface` → `PutObject item`
  - Items: RemoteControl, Pen, Book, KeyChain, Watch, Newspaper  
  - All item masses are within `robot2` capacity.

If parallelism is prioritized rather than minimizing robot count, `robot1` could perform SubTask 2 while `robot2` performs SubTask 3. However, the original required SubTask 1 remains impossible due to the missing `CleanObject` skill.