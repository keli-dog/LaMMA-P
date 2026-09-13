# GENERAL TASK DECOMPOSITION  
Decompose and parallelize subtasks wherever possible.

**Task Description:** Stage ingredients for future consumption.

This task involves preparing ingredients (e.g., slicing, cleaning) and placing them at a designated staging area (e.g., a countertop or bowl) so they are ready for later use. Each ingredient can be handled independently, so preparation and staging of different ingredients can be performed in parallel by multiple robots.

---

## Independent Subtasks

- **SubTask A:** Prepare and stage **Ingredient 1** (e.g., lettuce, tomato, bread, etc.).  
- **SubTask B:** Prepare and stage **Ingredient 2**.  
- **SubTask C:** Prepare and stage **Ingredient 3**.  
- ... (repeat for all required ingredients)

These subtasks are fully independent: each one involves moving to the ingredient's source location, optionally slicing/cleaning it, picking it up, moving to the staging area, and placing it there. They can be executed concurrently by different robots.

---

## Detailed Action Sequence for Each Ingredient Subtask

The following template applies to each ingredient. Replace `?ingredient` with the actual object name, and `?staging_location` with the designated staging area (e.g., `CounterTop`, `DiningTable`, or a bowl).

### SubTask i: Prepare and Stage `?ingredient`

1. **GoToObject** – Robot goes to the ingredient’s source location.  
   - Parameters: `?robot`, `?ingredient`  
   - Preconditions: `(not (inaction ?robot))`  
   - Effects: `(at ?robot ?ingredient)`, `(not (inaction ?robot))`

2. **SliceObject** (if the ingredient needs slicing) – Robot slices the ingredient at its source.  
   - Parameters: `?robot`, `?ingredient`, `?location` (the ingredient’s source location)  
   - Preconditions: `(at-location ?ingredient ?location)`, `(at ?robot ?location)`, `(not (inaction ?robot))`  
   - Effects: `(sliced ?ingredient)`, `(not (inaction ?robot))`

3. **CleanObject** (if the ingredient needs cleaning) – Robot cleans the ingredient at its source.  
   - Parameters: `?robot`, `?ingredient`  
   - Preconditions: `(at ?robot ?ingredient)`, `(not (inaction ?robot))`  
   - Effects: `(cleaned ?robot ?ingredient)`, `(not (inaction ?robot))`

4. **PickupObject** – Robot picks up the ingredient.  
   - Parameters: `?robot`, `?ingredient`, `?location`  
   - Preconditions: `(at-location ?ingredient ?location)`, `(at ?robot ?location)`, `(not (inaction ?robot))`  
   - Effects: `(holding ?robot ?ingredient)`, `(not (inaction ?robot))`

5. **GoToObject** – Robot moves to the staging area.  
   - Parameters: `?robot`, `?staging_location`  
   - Preconditions: `(not (inaction ?robot))`  
   - Effects: `(at ?robot ?staging_location)`, `(not (inaction ?robot))`

6. **PutObject** – Robot places the ingredient at the staging location.  
   - Parameters: `?robot`, `?ingredient`, `?staging_location`  
   - Preconditions: `(holding ?robot ?ingredient)`, `(at ?robot ?staging_location)`, `(not (inaction ?robot))`  
   - Effects: `(at-location ?ingredient ?staging_location)`, `(not (holding ?robot ?ingredient))`, `(not (inaction ?robot))`

> **Note:** If an ingredient is already sliced or cleaned (based on the initial state), steps 2 and/or 3 can be omitted.

---

## Parallelization Strategy

- If multiple robots are available, assign different ingredients to different robots to execute their respective subtasks concurrently.  
- All subtasks are independent because they operate on distinct objects and do not share preconditions with each other.  
- The only shared resource is the staging area; placing objects there can be done concurrently as long as the robot physically reaches it (no mutual exclusion expressed in the domain).

---

## Completion Criterion

The task is done when all required ingredients have the predicates `sliced` or `cleaned` (as needed) and are all located at the staging area via `at-l