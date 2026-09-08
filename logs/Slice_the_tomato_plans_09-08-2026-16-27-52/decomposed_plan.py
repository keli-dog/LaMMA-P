# Task Description: Slice the tomato

# GENERAL TASK DECOMPOSITION
# Single atomic subtask — no parallelization needed.
# SubTask 1: Slice the Tomato. (Skills Required: GoToObject, SliceObject)

# Action description from domain for tasks required

## SubTask 1: Slice the Tomato

### Initial condition analysis:
# 1. Robot not at tomato location.
# 2. Robot not holding tomato.
# 3. Tomato is at some location (e.g., CounterTop).
# 4. Robot is not in action (default initial state).

---

**GoToObject (Robot, Tomato)**

Parameters: ?robot - robot, ?Tomato - object

Preconditions: (not (inaction ?robot))

Effects: (at ?robot ?Tomato), (not (inaction ?robot))

---

**SliceObject (Robot, Tomato, TomatoLocation)**