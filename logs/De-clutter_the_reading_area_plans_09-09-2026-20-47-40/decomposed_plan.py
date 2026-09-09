# Task Decomposition: De-clutter the Reading Area

## GENERAL TASK DECOMPOSITION
This task involves organizing a reading area by putting away scattered items. We'll decompose it into parallelizable subtasks based on the objects that need to be moved.

### Independent Subtasks:
1. **Put books on the shelf** (Skills: GoToObject, PickupObject, PutObject)
2. **Put pens in the drawer** (Skills: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
3. **Put remote on the side table** (Skills: GoToObject, PickupObject, PutObject)
4. **Put newspaper in recycling** (Skills: GoToObject, PickupObject, PutObject)

These subtasks can be parallelized as they don't depend on each other.

## Action Sequences for Each Subtask

### Subtask 1: Put books on the shelf
Initial conditions:
- Robot not holding book
- Robot not at book location
- Shelf is accessible

1. **GoToObject**(Robot, Book)
   - Parameters: ?robot=Robot, ?object=Book
   - Pre: (not (inaction Robot))
   - Eff: (at Robot Book), (not (inaction Robot))

2. **PickupObject**(Robot, Book, CoffeeTable)
   - Parameters: ?robot=Robot, ?object=Book, ?location=CoffeeTable
   - Pre: (at-location Book CoffeeTable), (at Robot CoffeeTable), (not (inaction Robot))
   - Eff: (holding Robot Book), (not (inaction Robot))

3. **GoToObject**(Robot, Shelf)
   - Parameters: ?robot=Robot, ?object=Shelf
   - Pre: (not (inaction Robot))
   - Eff: (at Robot Shelf), (not (inaction Robot))

4. **PutObject**(Robot, Book, Shelf)
   - Parameters: ?robot=Robot, ?object=Book, ?location=Shelf
   - Pre: (holding Robot Book), (at Robot Shelf), (not (inaction Robot))
   - Eff: (at-location Book Shelf), (not (holding Robot Book)), (not (inaction Robot))

### Subtask 2: Put pens in the drawer
Initial conditions:
- Robot not holding pen
- Drawer initially closed

1. **GoToObject**(Robot, Pen)
   - Parameters: ?robot=Robot, ?object=Pen
   - Pre: (not (inaction Robot))
   - Eff: (at Robot Pen), (not (inaction Robot))

2. **PickupObject**(Robot, Pen, SideTable)
   - Parameters: ?robot=Robot, ?object=Pen, ?location=SideTable
   - Pre: (at-location Pen SideTable), (at Robot SideTable), (not (inaction Robot))
   - Eff: (holding Robot Pen), (not (inaction Robot))

3. **GoToObject**(Robot, Drawer)
   - Parameters: ?robot=Robot, ?object=Drawer
   - Pre: (not (inaction Robot))
   - Eff: (at Robot Drawer), (not (inaction Robot))

4. **OpenObject**(Robot, Drawer)
   - Parameters: ?robot=Robot, ?object=Drawer
   - Pre: (not (inaction Robot)), (at Robot Drawer)
   - Eff: (object-open Robot Drawer), (not (inaction Robot))

5. **PutObject**(Robot, Pen, Drawer)
   - Parameters: ?robot=Robot, ?object=Pen, ?location=Drawer
   - Pre: (holding Robot Pen), (at Robot Drawer), (not (inaction Robot))
   - Eff: (at-location Pen Drawer), (not (holding Robot Pen)), (not (inaction Robot))

6. **CloseObject**(Robot, Drawer)
   - Parameters: ?robot=Robot, ?object=Drawer
   - Pre: (not (inaction Robot)), (at Robot Drawer)
   - Eff: (object-close Robot Drawer), (not (inaction Robot))

### Subtask 3: Put remote on the side table
Initial conditions:
- Robot not holding remote
- Remote initially on coffee table

1. **GoToObject**(Robot, RemoteControl)
   - Parameters: ?robot=Robot, ?object=RemoteControl
   - Pre: (not (inaction Robot))
   - Eff: (at Robot RemoteControl), (not (inaction Robot))

2. **PickupObject**(Robot, RemoteControl, CoffeeTable)
   - Parameters: ?robot=Robot, ?object=RemoteControl, ?location=C