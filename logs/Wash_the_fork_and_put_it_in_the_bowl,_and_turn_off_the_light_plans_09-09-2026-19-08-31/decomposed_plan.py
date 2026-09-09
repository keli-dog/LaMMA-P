# Task Decomposition: Wash the fork and put it in the bowl, and turn off the light

## Independent Subtasks:
1. **SubTask 1**: Wash the fork and put it in the bowl (Skills: GoToObject, PickupObject, CleanObject, PutObject)
2. **SubTask 2**: Turn off the light (Skills: GoToObject, SwitchOff)

These subtasks can be parallelized since they don't depend on each other.

## Action Sequence:

### Subtask 1: Wash Fork and Place in Bowl
1. **GoToObject**(robot, fork)
   - Pre: (not (inaction robot))
   - Eff: (at robot fork), (not (inaction robot))

2. **PickupObject**(robot, fork, fork_location)
   - Pre: (at-location fork fork_location), (at robot fork_location), (not (inaction robot))
   - Eff: (holding robot fork), (not (inaction robot))

3. **GoToObject**(robot, sink)
   - Pre: (not (inaction robot))
   - Eff: (at robot sink), (not (inaction robot))

4. **CleanObject**(robot, fork)
   - Pre: (at robot sink), (holding robot fork), (not (inaction robot))
   - Eff: (cleaned robot fork), (not (inaction robot))

5. **GoToObject**(robot, bowl)
   - Pre: (not (inaction robot))
   - Eff: (at robot bowl), (not (inaction robot))

6. **PutObject**(robot, fork, bowl)
   - Pre: (holding robot fork), (at robot bowl), (not (inaction robot))
   - Eff: (at-location fork bowl), (not (holding robot fork)), (not (inaction robot))

### Subtask 2: Turn Off Light
1. **GoToObject**(robot, light_switch)
   - Pre: (not (inaction robot))
   - Eff: (at robot light_switch), (not (inaction robot))

2. **SwitchOff**(robot, light_switch)
   - Pre: (not (inaction robot)), (at robot light_switch)
   - Eff: (switch-off robot light_switch), (not (inaction robot))

## Robot Assignment:
- robot3 (with Pickup/Put skills) should handle Subtask 1
- robot2 (with SwitchOn/SwitchOff skills) should handle Subtask 2

## Initial Conditions:
- Fork is at initial location (not being held)
- Bowl is at its location
- Sink is accessible
- Light switch is at its location
- Light is initially on (needs to be turned off)

## Final Conditions:
- Fork is cleaned and in bowl
- Light is turned off