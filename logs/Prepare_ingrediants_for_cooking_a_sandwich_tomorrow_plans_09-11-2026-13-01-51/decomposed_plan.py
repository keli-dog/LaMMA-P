# GENERAL TASK DECOMPOSITION

# Task Description: Prepare ingredients for cooking a sandwich tomorrow

Independent subtasks (can be parallelized):
- **SubTask 1:** Slice the Lettuce  
- **SubTask 2:** Slice the Tomato  
- **SubTask 3:** Slice the Bread  
- **SubTask 4:** Wash the Plate  

Subtasks 1–3 are independent of SubTask 4, so they can be executed in parallel if multiple robots are available.

---

## SubTask 1: Slice the Lettuce

**Skills Required:** GoToObject, PickupObject, PutObject, SliceObject

1. **GoToObject**  
   Parameters: `?robot`, `?lettuce_location`  
   Precondition: `(not (inaction ?robot))`  
   Effect: `(at ?robot ?lettuce_location)`, `(not (inaction ?robot))`

2. **PickupObject**  
   Parameters: `?robot`, `?lettuce`, `?lettuce_location`  
   Precondition: `(at-location ?lettuce ?lettuce_location)`, `(at ?robot ?lettuce_location)`, `(not (inaction ?robot))`  
   Effect: `(holding ?robot ?lettuce)`, `(not (inaction ?robot))`

3. **GoToObject**  
   Parameters: `?robot`, `?countertop`  
   Precondition: `(not (inaction ?robot))`  
   Effect: `(at ?robot ?countertop)`, `(not (inaction ?robot))`

4. **PutObject**  
   Parameters: `?robot`, `?lettuce`, `?countertop`  
   Precondition: `(holding ?robot ?lettuce)`, `(at ?robot ?countertop)`, `(not (inaction ?robot))`  
   Effect: `(at-location ?lettuce ?countertop)`, `(not (holding ?robot ?lettuce))`, `(not (inaction ?robot))`

5. **SliceObject**  
   Parameters: `?robot`, `?lettuce`, `?countertop`  
   Precondition: `(at-location ?lettuce ?countertop)`, `(at ?robot ?countertop)`, `(not (inaction ?robot))`  
   Effect: `(sliced ?lettuce)`, `(not (inaction ?robot))`

---

## SubTask 2: Slice the Tomato

**Skills Required:** GoToObject, PickupObject, PutObject, SliceObject

1. **GoToObject**  
   Parameters: `?robot`, `?tomato_location`  
   Precondition: `(not (inaction ?robot))`  
   Effect: `(at ?robot ?tomato_location)`, `(not (inaction ?robot))`

2. **PickupObject**  
   Parameters: `?robot`, `?tomato`, `?tomato_location`  
   Precondition: `(at-location ?tomato ?tomato_location)`, `(at ?robot ?tomato_location)`, `(not (inaction ?robot))`  
   Effect: `(holding ?robot ?tomato)`, `(not (inaction ?robot))`

3. **GoToObject**  
   Parameters: `?robot`, `?countertop`  
   Precondition: `(not (inaction ?robot))`  
   Effect: `(at ?robot ?countertop)`, `(not (inaction ?robot))`

4. **PutObject**  
   Parameters: `?robot`, `?tomato`, `?countertop`  
   Precondition: `(holding ?robot ?tomato)`, `(at ?robot ?countertop)`, `(not (inaction ?robot))`  
   Effect: `(at-location ?tomato ?countertop)`, `(not (holding ?robot ?tomato))`, `(not (inaction ?robot))`

5. **SliceObject**  
   Parameters: `?robot`, `?tomato`, `?countertop`  
   Precondition: `(at-location ?tomato ?countertop)`, `(at ?robot ?countertop)`, `(not (inaction ?robot))`  
   Effect: `(sliced ?tomato)`, `(not (inaction ?robot))`

---

## SubTask 3: Slice the Bread

**Skills Required:** GoToObject, PickupObject, PutObject, SliceObject

1. **GoToObject**  
   Parameters: `