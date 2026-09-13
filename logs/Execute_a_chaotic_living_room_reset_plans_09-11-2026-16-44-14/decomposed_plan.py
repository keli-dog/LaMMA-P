# GENERAL TASK DECOMPOSITION  
Decompose and parallel subtasks wherever possible.

# Task Description: Execute a chaotic living room reset

We assume the living room is in a state of disorder: items are scattered, devices are switched on, drawers/cabinets/fridge are left open, and soft furnishings are misplaced. The reset will restore order by turning off electronics, returning objects to their designated locations, closing any open compartments, and tidying furniture pieces.

**Independent subtasks** (can be executed in parallel by different robots):
- **SubTask 1**: Turn off all electronic devices and lights.  
  *Skills Required*: GoToObject, SwitchOff  
- **SubTask 2**: Collect scattered items and place them on their proper surfaces (table, shelf, drawer, etc.).  
  *Skills Required*: GoToObject, PickupObject, PutObject  
- **SubTask 3**: Close all open drawers, cabinets, and the fridge.  
  *Skills Required*: GoToObject, CloseObject, CloseFridge  
- **SubTask 4**: Tidy up soft furnishings (e.g., pillows, blankets) and place them neatly.  
  *Skills Required*: GoToObject, PickupObject, PutObject  

These subtasks do not depend on each other and can be assigned to separate robots for parallel execution.

---

## SubTask 1: Turn Off All Electronic Devices and Lights  
**Goal**: Switch off any device or light that is currently on (e.g., Television, FloorLamp, LightSwitch).  

**Skills**: GoToObject, SwitchOff  

**Action Sequence** (repeated for each device):

1. **GoToObject**  
   Parameters: ?robot, ?device  
   Precondition: (not (inaction ?robot))  
   Effect: (at ?robot ?device)

2. **SwitchOff**  
   Parameters: ?robot, ?device  
   Precondition: (at ?robot ?device), (not (inaction ?robot))  
   Effect: (switch-off ?robot ?device)

**Parallelization**: Different robots can handle different devices simultaneously.

---

## SubTask 2: Collect and Place Scattered Items on Appropriate Surfaces  
**Goal**: Return all misplaced objects (e.g., Book, RemoteControl, Pillow, Vase) to their designated spots (e.g., Shelf, CoffeeTable, Drawer, SideTable).  

**Skills**: GoToObject, PickupObject, PutObject  

**Action Sequence** (for each misplaced item ?obj with destination ?dest):  

1. **GoToObject**  
   Parameters: ?robot, ?obj  
   Precondition: (not (inaction ?robot))  
   Effect: (at ?robot ?obj)

2. **PickupObject**  
   Parameters: ?robot, ?obj, ?currentLocation  
   Precondition: (at-location ?obj ?currentLocation), (at ?robot ?currentLocation), (not (inaction ?robot))  
   Effect: (holding ?robot ?obj)

3. **GoToObject**  
   Parameters: ?robot, ?dest  
   Precondition: (not (inaction ?robot))  
   Effect: (at ?robot ?dest)

4. **PutObject**  
   Parameters: ?robot, ?obj, ?dest  
   Precondition: (holding ?robot ?obj), (at ?robot ?dest), (not (inaction ?robot))  
   Effect: (at-location ?obj ?dest), (not (holding ?robot ?obj))

**Note**: For objects that belong in drawers, you may first need to open the drawer (OpenObject) and close it after placing the item (CloseObject). This can be integrated if the drawer is closed initially.

**Parallelization**: Robots can pick different objects and work concurrently.

---

## SubTask 3: Close All Open Drawers, Cabinets, and the Fridge  
**Goal**: Ensure every compartment (drawer, cabinet, fridge) is closed.  

**Skills**: GoToObject, CloseObject, CloseFridge  

**Action Sequence** (for each open compartment ?comp):

1. **GoToObject**  
   Parameters: ?robot, ?comp  
   Precondition: (not (inaction ?robot))  
   Effect: (at ?robot ?comp)

2. **If ?comp is a fridge**:  
   - **CloseFridge**  
     Parameters: ?robot, ?comp  
     Precondition: (at ?robot ?comp), (object-open ?robot ?comp), (is-fridge ?comp), (not (inaction ?robot))  
     Effect: (object-close ?robot ?comp), (decrease (fridge-state ?comp) 1)  

   **Else**