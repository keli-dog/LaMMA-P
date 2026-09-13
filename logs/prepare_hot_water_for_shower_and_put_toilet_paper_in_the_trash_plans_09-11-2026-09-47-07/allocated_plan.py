## TASK ALLOCATION

### Step 1: Identify Subtasks and Required Skills

**SubTask 1: Prepare Hot Water for Shower**  
- Actions: Go to LightSwitch → SwitchOn LightSwitch → Go to Faucet → SwitchOn Faucet  
- Skills Required: `GoToObject`, `SwitchOn`

**SubTask 2: Put Toilet Paper in the Trash**  
- Actions: Go to ToiletPaper → PickupObject ToiletPaper → Go to GarbageCan → PutObject ToiletPaper in GarbageCan  
- Skills Required: `GoToObject`, `PickupObject`, `PutObject`

---

### Step 2: Determine Dependencies and Parallelization

- SubTask 1 and SubTask 2 are **independent** of each other.  
- They can be performed **in parallel** by two different robots.  
- Within each subtask, the actions must be performed **sequentially** because each action depends on the previous one (e.g., the robot must pick up the toilet paper before putting it in the trash).

---

### Step 3: Assign Robots Based on Skills and Mass Capacity

| Subtask | Required Skills | Assigned Robot | Robot Skills | Robot Mass Capacity | Object Mass Involved | Capacity Check |
|---|---|---|---|---|---|---|
| SubTask 1: Prepare Hot Water for Shower | GoToObject, SwitchOn | **robot2** | GoToObject, SwitchOn, SwitchOff | 100 | LightSwitch: 0.0, Faucet: 0.0 | ✅ within capacity |
| SubTask 2: Put Toilet Paper in Trash | GoToObject, PickupObject, PutObject | **robot3** | GoToObject, PickupObject, PutObject | 100 | ToiletPaper: 0.2, GarbageCan: 0.7 | ✅ within capacity |

- **robot1** and **robot4** are not needed because robot2 and robot3 already possess all required skills for the subtasks.  
- No robot team is required, because each subtask can be completed individually by a robot with the needed skills.  
- The minimum number of robots used is **2**.

---

### Final Allocation

- **robot2** performs SubTask 1: Prepare Hot Water for Shower  
  - GoToObject LightSwitch  
  - SwitchOn LightSwitch  
  - GoToObject Faucet  
  - SwitchOn Faucet  

- **robot3** performs SubTask 2: Put Toilet Paper in the Trash  
  - GoToObject ToiletPaper  
  - PickupObject ToiletPaper  
  - GoToObject GarbageCan  
  - PutObject ToiletPaper in GarbageCan  

These two subtasks run **in parallel** and the overall task is completed when both robots finish their assigned subtasks.