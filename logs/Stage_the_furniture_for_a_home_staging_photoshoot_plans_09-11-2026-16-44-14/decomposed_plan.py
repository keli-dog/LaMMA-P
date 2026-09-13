# GENERAL TASK DECOMPOSITION 
Decompose and parallel subtasks where ever possible.

## Task Description: Stage the furniture for a home staging photoshoot

**Interpretation:**  
For a successful home staging, the environment must be visually appealing: surfaces clean, lights turned on, and small decorative items arranged neatly on tables and shelves. Heavy furniture cannot be moved by the robots (mass capacities 0.4 and 0.9 kg) – all furniture items exceed 1 kg – so the staging focuses on cleaning, lighting, and placement of lightweight accessories.

**Independent Subtasks:**
- **SubTask 1:** Clean all furniture surfaces (Sofa, CoffeeTable, SideTable, Dresser, Drawer, Shelf, etc.).  
- **SubTask 2:** Turn on all applicable lights (FloorLamp, LightSwitch) for a bright, inviting atmosphere.  
- **SubTask 3:** Place small decorative items (RemoteControl, Pen, Book, KeyChain, Watch, Newspaper) on appropriate surfaces to create a styled look.

SubTasks 1 and 2 are independent and can be executed in parallel by different robots. SubTask 3 can also run in parallel after SubTasks 1 and 2 if the robots are available, but some placements may depend on cleaned surfaces (so we keep it as a separate phase).

---

## SubTask 1: Clean All Furniture Surfaces

**Skill Requirements:** GoToObject, CleanObject  
**Robots:** robot1, robot2 (split surfaces)

### Initial Condition Analysis:
1. Robots are initially idle (`not (inaction ?robot)`).
2. Robots are not at any furniture location initially.
3. Furniture objects are present: Sofa, CoffeeTable, SideTable, Dresser, Drawer (×4), Shelf.

### Action Sequences:

#### For robot1 (cleaning Sofa and CoffeeTable)
1. **GoToObject:** Robot goes to the Sofa.  
   Parameters: ?robot = robot1, ?object = Sofa  
   Preconditions: (not (inaction robot1))  
   Effects: (at robot1 Sofa), (not (inaction robot1))

2. **CleanObject:** Robot cleans the Sofa.  
   Parameters: ?robot = robot1, ?object = Sofa  
   Preconditions: (at robot1 Sofa), (not (inaction robot1))  
   Effects: (cleaned robot1 Sofa), (not (inaction robot1))

3. **GoToObject:** Robot goes to the CoffeeTable.  
   Parameters: ?robot = robot1, ?object = CoffeeTable  
   Preconditions: (not (inaction robot1))  
   Effects: (at robot1 CoffeeTable), (not (inaction robot1))

4. **CleanObject:** Robot cleans the CoffeeTable.  
   Parameters: ?robot = robot1, ?object = CoffeeTable  
   Preconditions: (at robot1 CoffeeTable), (not (inaction robot1))  
   Effects: (cleaned robot1 CoffeeTable), (not (inaction robot1))

#### For robot2 (cleaning SideTable, Dresser, Drawers, Shelf)
5. **GoToObject:** Robot goes to the SideTable.  
   Parameters: ?robot = robot2, ?object = SideTable  
   Preconditions: (not (inaction robot2))  
   Effects: (at robot2 SideTable), (not (inaction robot2))

6. **CleanObject:** Robot cleans the SideTable.  
   Parameters: ?robot = robot2, ?object = SideTable  
   Preconditions: (at robot2 SideTable), (not (inaction robot2))  
   Effects: (cleaned robot2 SideTable), (not (inaction robot2))

7. **GoToObject:** Robot goes to the Dresser.  
   Parameters: ?robot = robot2, ?object = Dresser  
   Preconditions: (not (inaction robot2))  
   Effects: (at robot2 Dresser), (not (inaction robot2))

8. **CleanObject:** Robot cleans the Dresser.  
   Parameters: ?robot = robot2, ?object = Dresser  
   Preconditions: (at robot2 Dresser), (not (inaction robot2))  
   Effects: (cleaned robot2 Dresser), (not (inaction robot2))

9. **GoToObject:** Robot goes to the Drawer (first).  
   Parameters: ?robot = robot2, ?object = Drawer  
   Preconditions: (not (inaction robot2))  
   Effects: (at robot2 Drawer), (not (inaction robot2))

10. **CleanObject:** Robot cleans the Drawer.  
    Parameters