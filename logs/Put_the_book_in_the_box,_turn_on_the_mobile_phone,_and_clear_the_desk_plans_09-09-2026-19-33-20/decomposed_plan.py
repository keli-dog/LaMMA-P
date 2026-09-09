# Task Decomposition: Put the book in the box, turn on the mobile phone, and clear the desk

## Independent Subtasks:
1. **SubTask 1**: Put the book in the box (Skills: GoToObject, PickupObject, PutObject)
2. **SubTask 2**: Turn on the mobile phone (Skills: GoToObject, SwitchOn)
3. **SubTask 3**: Clear the desk (Skills: GoToObject, PickupObject, PutObject)

These subtasks can be parallelized as they don't depend on each other.

## Action Sequences:

### Subtask 1: Put the book in the box
1. **GoToObject**(robot, book)
   - Pre: (not (inaction robot))
   - Eff: (at robot book), (not (inaction robot))

2. **PickupObject**(robot, book, book_location)
   - Pre: (at-location book book_location), (at robot book_location), (not (inaction robot))
   - Eff: (holding robot book), (not (inaction robot))

3. **GoToObject**(robot, box)
   - Pre: (not (inaction robot))
   - Eff: (at robot box), (not (inaction robot))

4. **PutObject**(robot, book, box)
   - Pre: (holding robot book), (at robot box), (not (inaction robot))
   - Eff: (at-location book box), (not (holding robot book)), (not (inaction robot))

### Subtask 2: Turn on the mobile phone
1. **GoToObject**(robot, cellphone)
   - Pre: (not (inaction robot))
   - Eff: (at robot cellphone), (not (inaction robot))

2. **SwitchOn**(robot, cellphone)
   - Pre: (not (inaction robot)), (at robot cellphone)
   - Eff: (switch-on robot cellphone), (not (inaction robot))

### Subtask 3: Clear the desk
1. **GoToObject**(robot, desk)
   - Pre: (not (inaction robot))
   - Eff: (at robot desk), (not (inaction robot))

2. **PickupObject**(robot, object_on_desk, desk)
   - Pre: (at-location object_on_desk desk), (at robot desk), (not (inaction robot))
   - Eff: (holding robot object_on_desk), (not (inaction robot))

3. **GoToObject**(robot, shelf)
   - Pre: (not (inaction robot))
   - Eff: (at robot shelf), (not (inaction robot))

4. **PutObject**(robot, object_on_desk, shelf)
   - Pre: (holding robot object_on_desk), (at robot shelf), (not (inaction robot))
   - Eff: (at-location object_on_desk shelf), (not (holding robot object_on_desk)), (not (inaction robot))

## Parallel Execution Possibilities:
- Robot1 can handle Subtask 1 (book in box)
- Robot2 can handle Subtask 2 (turn on phone)
- Robot3 can handle Subtask 3 (clear desk)

All three robots can work simultaneously since there are no dependencies between these tasks.

## Initial Conditions:
- All robots start with (not (inaction robot))
- Book is at its initial location (at-location book book_location)
- Cellphone is at its location (at-location cellphone cellphone_location)
- Objects are on the desk (at-location object_on_desk desk)
- Box is at its location (at-location box box_location)
- Shelf is empty (no initial objects on it)