# SOLUTION
All three robots have the same complete skill set, including `GoToObject`, `OpenObject`, `CloseObject`, `SwitchOn`, `SwitchOff`, `PickupObject`, and `PutObject`. Each robot also has a mass capacity of 100, and the objects involved in these reset subtasks are below this capacity (e.g., Television 9.83, FloorLamp 3.93, Laptop 2.3, Pillow 0.7, Vases 1.0). The Sofa is not treated as a soft furnishing to be picked up in this reset; if it were necessary to move the Sofa, a team of two robots would be required because its mass is 103.999 kg, but this is not part of the stated tidy-soft-furnishings task.

Subtasks 1–4 are independent, so they can be performed in parallel. Since there are 4 subtasks and only 3 robots, one robot will perform two subtasks sequentially.

- **Robot1**: SubTask 1 — Turn off all electronic devices and lights.  
  Then, after finishing SubTask 1, Robot1 performs SubTask 4 — Tidy soft furnishings.

- **Robot2**: SubTask 2 — Collect scattered items and place them on proper surfaces.

- **Robot3**: SubTask 3 — Close all open drawers, cabinets, and the fridge.

All robots start simultaneously. No robot team is required, and every subtask is within the assigned robot’s skills and mass capacity. If a robot places objects into a drawer/cabinet during SubTask 2, Robot3 should close that compartment after the placement, or Robot2 can close it immediately after placing the object.