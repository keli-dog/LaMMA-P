# GENERAL TASK DECOMPOSITION

Decompose and parallelize subtasks wherever possible.

# Task Description: Execute a deep clean and waste disposal cycle

**Independent subtasks:**
- **SubTask 1: Clean all dirty items and surfaces**  
  (Skills Required: GoToObject, CleanObject)
- **SubTask 2: Dispose of waste and garbage**  
  (Skills Required: GoToObject, PickupObject, PutObject)

We can parallelize SubTask 1 and SubTask 2 because they do not depend on each other and can be performed concurrently by different robots.

---

## SubTask 1: Clean All Dirty Items and Surfaces

### Initial Condition Analysis
- Robot is not currently cleaning any target object.
- Robot is not holding any cleaning supplies.
- All dirty items are at their respective locations.

### Actions for each dirty item (repeat for each: Plate, Cup, Pan, Pot, CounterTop, Sink, etc.)

1. **GoToObject** – Robot goes to the item.  
   Parameters: `?robot` - robot, `?item` - object  
   Preconditions: `(not (inaction ?robot))`  
   Effects: `(at ?robot ?item)`, `(not (inaction ?robot))`

2. **CleanObject** – Robot cleans the item.  
   Parameters: `?robot` - robot, `?item` - object  
   Preconditions: `(at ?robot ?item)`, `(not (inaction ?robot))`  
   Effects: `(cleaned ?robot ?item)`, `(not (inaction ?robot))`

Repeat for all items requiring cleaning. This task can be performed by one or more robots, each handling a subset of the items.

---

## SubTask 2: Dispose of Waste and Garbage

### Initial Condition Analysis
- Robot is not at the location of any waste item.
- Robot is not holding any waste.
- Garbage can is empty and accessible.

### Actions for each waste item (e.g., leftover food, trash, GarbageBag)

1. **GoToObject** – Robot goes to the waste item.  
   Parameters: `?robot` - robot, `?garbage` - object  
   Preconditions: `(not (inaction ?robot))`  
   Effects: `(at ?robot ?garbage)`, `(not (inaction ?robot))`

2. **PickupObject** – Robot picks up the waste item.  
   Parameters: `?robot` - robot, `?garbage` - object, `?location` - object (location of waste)  
   Preconditions: `(at-location ?garbage ?location)`, `(at ?robot ?location)`, `(not (inaction ?robot))`  
   Effects: `(holding ?robot ?garbage)`, `(not (inaction ?robot))`

3. **GoToObject** – Robot goes to the garbage can.  
   Parameters: `?robot` - robot, `?GarbageCan` - object  
   Preconditions: `(not (inaction ?robot))`  
   Effects: `(at ?robot ?GarbageCan)`, `(not (inaction ?robot))`

4. **PutObject** – Robot disposes of the waste in the garbage can.  
   Parameters: `?robot` - robot, `?garbage` - object, `?GarbageCan` - object  
   Preconditions: `(holding ?robot ?garbage)`, `(at ?robot ?GarbageCan)`, `(not (inaction ?robot))`  
   Effects: `(at-location ?garbage ?GarbageCan)`, `(not (holding ?robot ?garbage))`, `(not (inaction ?robot))`

Repeat for all waste items. If a garbage bag is full, it may also be taken to the garbage can and disposed of similarly.

---

# Task Complete

After both subtasks are accomplished, all items are cleaned and waste has been disposed of, fulfilling the deep clean and waste disposal cycle.