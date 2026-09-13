## General Task Decomposition: De-clutter the Reading Area

De-cluttering the reading area means moving misplaced objects from the reading area to appropriate storage locations. The subtasks below are independent and can be parallelized using different robots, as long as each robot can carry the assigned objects within its mass capacity and no two robots try to occupy the same storage target at the same time.

### Suggested independent subtasks

1. **Put small stationery / personal items in a Drawer**  
   - Objects: `Pen`, `CreditCard`, `KeyChain`, `Watch`, `RemoteControl`  
   - Target: a `Drawer`  
   - Skills: `GoToObject`, `PickupObject`, `OpenObject`, `PutObject`, `CloseObject`

2. **Put reading materials on a Shelf or into GarbageCan**  
   - Objects: `Book`, `Newspaper`  
   - Targets: `Shelf` for `Book`; `GarbageCan` for `Newspaper`  
   - Skills: `GoToObject`, `PickupObject`, `PutObject`  
   - (If the GarbageCan has a lid, use `OpenObject` and `CloseObject`.)

3. **Return soft/decorative items to their proper places**  
   - Objects: `Pillow`, `Vase`, `Statue`  
   - Targets: `Sofa` for `Pillow`; `SideTable` / `Shelf` for `Vase`; `Shelf` / `SideTable` for `Statue`  
   - Skills: `GoToObject`, `PickupObject`, `PutObject`

4. **Move electronic clutter to a SideTable/Shelf**  
   - Object: `Laptop`  
   - Target: `SideTable` or `Shelf`  
   - Skills: `GoToObject`, `PickupObject`, `PutObject`

> **Parallelization note:**  
> Subtasks 1, 2, 3, and 4 are independent. Assign different robots to different subtasks. For example:
> - `robot1` can handle the light stationery items (`Pen`, `CreditCard`, `KeyChain`, `Watch`, `RemoteControl`).
> - `robot4` (the 0.9 kg robot) can handle `Book`, `Newspaper`, and `Pillow`.
> - `robot2` (5 kg capacity) can handle heavier items: `Laptop`, `Vase`, `Statue`.
> - `robot3` can be used only for very tiny items like `Pen` or `CreditCard`.

---

### Action sequence for each subtask

#### Subtask 1: Put small items in a Drawer
For each small item, e.g. `Pen`, `CreditCard`, etc.:

1. `GoToObject(robot, item)`  
2. `PickupObject(robot, item, current_location)`  
3. `GoToObject(robot, target_drawer)`  
4. `OpenObject(robot, target_drawer)` — if the drawer is closed  
5. `PutObject(robot, item, target_drawer)`  
6. `CloseObject(robot, target_drawer)` — if it was opened  

#### Subtask 2: Put reading material away
For `Book`:

1. `GoToObject(robot, Book)`  
2. `PickupObject(robot, Book, current_location)`  
3. `GoToObject(robot, Shelf)`  
4. `PutObject(robot, Book, Shelf)`  

For `Newspaper`:

1. `GoToObject(robot, Newspaper)`  
2. `PickupObject(robot, Newspaper, current_location)`  
3. `GoToObject(robot, GarbageCan)`  
4. `PutObject(robot, Newspaper, GarbageCan)`  

#### Subtask 3: Return soft/decorative items
For each object (`Pillow`, `Vase`, `Statue`):

1. `GoToObject(robot, object)`  
2. `PickupObject(robot, object, current_location)`  
3. `GoToObject(robot, target_location)`  
4. `PutObject(robot, object, target_location)`  

Targets:  
- `Pillow` → `Sofa`  
- `Vase` → `SideTable` or `Shelf`  
- `Statue` → `Shelf` or `SideTable`

#### Subtask 4: Move Laptop
1. `GoToObject(robot, Laptop)`  
2. `PickupObject(robot, Laptop, current_location)`  
3. `GoToObject