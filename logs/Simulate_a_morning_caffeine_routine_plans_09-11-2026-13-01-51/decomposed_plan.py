# GENERAL TASK DECOMPOSITION 
Decompose and parallel subtasks where ever possible.

# Task Description: Simulate a morning caffeine routine

Independent subtasks:

- **SubTask 1: Prepare Coffee** (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)  
- **SubTask 2: Prepare Tea** (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)  
- **SubTask 3: Set up a Mug** (Skills Required: GoToObject, PickupObject, PutObject)

These subtasks are independent and can be executed in parallel because they do not depend on each other’s outcome.

---

## SubTask 1: Prepare Coffee

**Initial condition analysis:**  
1. Robot not at the mug location.  
2. Robot not holding the mug.  
3. Coffee machine is present and operational.

### Action Sequence

**GoToObject** (Robot, Mug)  
- Parameters: ?robot, ?mug  
- Preconditions: `(not (inaction ?robot))`  
- Effects: `(at ?robot ?mug)`, `(not (inaction ?robot))`

**PickupObject** (Robot, Mug, MugLocation)  
- Parameters: ?robot, ?mug, ?mugLocation  
- Preconditions: `(at-location ?mug ?mugLocation)`, `(at ?robot ?mugLocation)`, `(not (inaction ?robot))`  
- Effects: `(holding ?robot ?mug)`, `(not (inaction ?robot))`

**GoToObject** (Robot, CoffeeMachine)  
- Parameters: ?robot, ?coffeeMachine  
- Preconditions: `(not (inaction ?robot))`  
- Effects: `(at ?robot ?coffeeMachine)`, `(not (inaction ?robot))`

**SwitchOn** (Robot, CoffeeMachine)  
- Parameters: ?robot, ?coffeeMachine  
- Preconditions: `(not (inaction ?robot))`, `(at ?robot ?coffeeMachine)`  
- Effects: `(switch-on ?robot ?coffeeMachine)`, `(not (inaction ?robot))`

**SwitchOff** (Robot, CoffeeMachine)  
- Parameters: ?robot, ?coffeeMachine  
- Preconditions: `(not (inaction ?robot))`, `(at ?robot ?coffeeMachine)`  
- Effects: `(switch-off ?robot ?coffeeMachine)`, `(not (inaction ?robot))`

**PutObject** (Robot, Mug, CounterTop)  
- Parameters: ?robot, ?mug, ?counterTop  
- Preconditions: `(holding ?robot ?mug)`, `(at ?robot ?counterTop)`, `(not (inaction ?robot))`  
- Effects: `(at-location ?mug ?counterTop)`, `(not (holding ?robot ?mug))`, `(not (inaction ?robot))`

---

## SubTask 2: Prepare Tea

**Initial condition analysis:**  
1. Robot not at the kettle location.  
2. Robot not holding the kettle.  
3. Kettle and stove are available.

### Action Sequence

**GoToObject** (Robot, Kettle)  
- Parameters: ?robot, ?kettle  
- Preconditions: `(not (inaction ?robot))`  
- Effects: `(at ?robot ?kettle)`, `(not (inaction ?robot))`

**PickupObject** (Robot, Kettle, KettleLocation)  
- Parameters: ?robot, ?kettle, ?kettleLocation  
- Preconditions: `(at-location ?kettle ?kettleLocation)`, `(at ?robot ?kettleLocation)`, `(not (inaction ?robot))`  
- Effects: `(holding ?robot ?kettle)`, `(not (inaction ?robot))`

**GoToObject** (Robot, StoveBurner)  
- Parameters: ?robot, ?stoveBurner  
- Preconditions: `(not (inaction ?robot))`  
- Effects: `(at ?robot ?stoveBurner)`, `(not (inaction ?robot))`

**PutObject** (Robot, Kettle, StoveBurner)  
- Parameters: ?robot, ?kettle, ?stoveBurner  
- Preconditions: `(holding ?robot ?kettle)`, `(at ?robot ?stoveBurner)`, `(not (inaction ?robot))`  
- Effects: `(at-location