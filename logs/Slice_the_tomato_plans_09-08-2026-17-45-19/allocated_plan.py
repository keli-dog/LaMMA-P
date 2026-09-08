Given the task of slicing a tomato, we need to break down the task into subtasks and allocate robots based on their skills and mass capacity. Here are the steps involved:

### Task Decomposition:
1. **Go to Tomato**: Move to the location of the tomato.
2. **Pick up Tomato**: Pick up the tomato.
3. **Go to Cutting Board**: Move to a location where slicing can be performed (e.g., a cutting board).
4. **Slice Tomato**: Slice the tomato.

### Robot Skills and Mass Capacity:
- All robots have the necessary skills (`GoToObject`, `PickupObject`, `SliceObject`).
- All robots have a mass capacity of 100, which is more than sufficient for handling the tomato (mass: 0.12).

### Task Allocation:
Since all three robots have the necessary skills and mass capacity, we can allocate any one of them to perform the task. For simplicity and efficiency, we will assign the task to `robot1`.

### Detailed Action Sequence:
1. **GoToObject (Robot1, Tomato)**
   - Move `robot1` to the location of the tomato.
2. **PickupObject (Robot1, Tomato)**
   - Pick up the tomato.
3. **GoToObject (Robot1, CuttingBoard)**
   - Move `robot1` to the cutting board.
4. **SliceObject (Robot1, Tomato)**
   - Slice the tomato.

### PDDL Representation:
```pddl
(define (problem slice_tomato)
  (:domain allactionrobot)
  (:objects
    robot1 - robot
    tomato - object
    cuttingBoard - object
    tomatoLocation - object
  )
  (:init
    (not (inaction robot1))
    (at-location tomato tomatoLocation)
  )
  (:goal
    (and
      (sliced tomato)
      (not (holding robot1 tomato))
    )
  )
)
```

### Explanation:
- **Initial State**: The robot is not inaction, and the tomato is located at `tomatoLocation`.
- **Goal**: The tomato should be sliced, and the robot should not be holding the tomato.

### Action Execution:
1. **GoToObject (Robot1, Tomato)**
   - Move `robot1` to the location of the tomato.
2. **PickupObject (Robot1, Tomato)**
   - Pick up the tomato.
3. **GoToObject (Robot1, CuttingBoard)**
   - Move `robot1` to the cutting board.
4. **SliceObject (Robot1, Tomato)**
   - Slice the tomato.

### Summary:
- **Robot Allocation**: `robot1` is assigned to perform all subtasks.
- **Subtask Execution**: The subtasks are executed sequentially by `robot1`.

This solution ensures that the task is performed efficiently using the minimum number of robots necessary and adheres to the constraints of skills and mass capacity.