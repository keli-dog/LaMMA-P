SOLUTION

All three robots have identical skills and mass capacity, so no robot team is required. Each robot individually has every skill needed for its assigned subtask, and each robot’s mass capacity is 100, which is greater than the mass of any object involved in the subtasks.

Required skills per subtask:

- **Subtask 1: Turn off all appliances and lights** → `GoToObject`, `SwitchOff`
- **Subtask 2: Close all cabinets, drawers, windows, and blinds** → `GoToObject`, `CloseObject`
- **Subtask 3: Ensure the refrigerator is closed** → `GoToObject`, `CloseObject` / `CloseFridge`

The three subtasks are **independent** and can be executed **in parallel**.

### Task Allocation

| Robot | Assigned Subtask | Actions |
|---|---|---|
| **Robot1** | Subtask 1: Turn off appliances and lights | Go to each appliance/light switch and use `SwitchOff` on: CoffeeMachine, Microwave, Toaster, StoveKnobs, LightSwitch, etc. |
| **Robot2** | Subtask 2: Close cabinets, drawers, windows, and blinds | Go to each object and use `CloseObject` on: all Cabinets, Drawers, Window, Blinds. |
| **Robot3** | Subtask 3: Ensure refrigerator is closed | Go to Fridge; if open, use `CloseObject` / `CloseFridge`; if already closed, take no action. |

All robots can start immediately and perform their subtasks in parallel. The mass of all target objects is well within each robot’s mass capacity of 100.