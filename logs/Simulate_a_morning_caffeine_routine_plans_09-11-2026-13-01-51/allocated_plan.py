# SOLUTION

Available robots:

- **robot2**: `GoToObject`, `PickupObject`, `PutObject` — mass capacity 100
- **robot3 (Break/Throw)**: `GoToObject`, `BreakObject`, `ThrowObject` — mass capacity 100 (not needed)
- **robot3 (Switch)**: `GoToObject`, `SwitchOn`, `SwitchOff` — mass capacity 100

Skill analysis:

- **SubTask 1: Prepare Coffee** requires `GoToObject`, `PickupObject`, `PutObject`, `SwitchOn`, `SwitchOff`.  
  No single robot has all these skills. A team of **robot2 + robot3 (Switch)** collectively has all required skills.

- **SubTask 2: Prepare Tea** requires the same skill set: `GoToObject`, `PickupObject`, `PutObject`, `SwitchOn`, `SwitchOff`.  
  It also requires the team of **robot2 + robot3 (Switch)**.

- **SubTask 3: Set up a Mug** requires `GoToObject`, `PickupObject`, `PutObject`.  
  **robot2** alone has all these skills.

Because **robot2** is needed for every subtask, and the coffee/tea subtasks also need **robot3 (Switch)**, these subtasks cannot be executed in parallel with the available robots. They must be performed sequentially.

Allocation:

1. **Set up a Mug** → **robot2**
2. **Prepare Coffee** → **robot2 + robot3 (Switch)**
3. **Prepare Tea** → **robot2 + robot3 (Switch)**

The order can be adjusted, but only one subtask can be active at a time.  
**robot3 (Break/Throw)** is unused because no subtask requires `BreakObject` or `ThrowObject`.

Mass capacity check: All objects involved have masses well below the 100-unit capacity of the robots/team, so no mass constraint is violated.

Minimum robots used: **2**.