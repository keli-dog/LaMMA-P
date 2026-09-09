# Task Analysis: Put the Box on the Sofa and the Bowl in the Box

## GENERAL TASK DECOMPOSITION
This task can be decomposed into two parallel subtasks since they don't have dependencies on each other:
1. SubTask 1: Put the Box on the Sofa
2. SubTask 2: Put the Bowl in the Box

## Required Skills
- GoToObject
- PickupObject
- PutObject

## Objects Needed
- Box (mass: 0.3)
- Bowl (mass: 0.47)
- Sofa (mass: 104.0)

## Robot Selection
Both robots can handle this task since:
- robot1 can carry up to 0.4kg (can handle box and bowl)
- robot2 can carry up to 1.0kg (can handle box and bowl)

# Subtask 1: Put the Box on the Sofa

## Initial Conditions
1. Robot not holding box
2. Robot not at box location
3. Box not on sofa initially

## Action Sequence

1. **GoToObject** (robot, box)
   - Parameters: ?robot, ?box
   - Preconditions: (not (inaction ?robot))
   - Effects: (at ?robot ?box), (not (inaction ?robot))

2. **PickupObject** (robot, box, box_location)
   - Parameters: ?robot, ?box, ?box_location
   - Preconditions: (at-location ?box ?box_location), (at ?robot ?box_location), (not (inaction ?robot))
   - Effects: (holding ?robot ?box), (not (inaction ?robot))

3. **GoToObject** (robot, sofa)
   - Parameters: ?robot, ?sofa
   - Preconditions: (not (inaction ?robot))
   - Effects: (at ?robot ?sofa), (not (inaction ?robot))

4. **PutObject** (robot, box, sofa)
   - Parameters: ?robot, ?box, ?sofa
   - Preconditions: (holding ?robot ?box), (at ?robot ?sofa), (not (inaction ?robot))
   - Effects: (at-location ?box ?sofa), (not (holding ?robot ?box)), (not (inaction ?robot))

# Subtask 2: Put the Bowl in the Box

## Initial Conditions
1. Robot not holding bowl
2. Robot not at bowl location
3. Bowl not in box initially
4. Box must be on sofa first (dependency from Subtask 1)

## Action Sequence

1. **GoToObject** (robot, bowl)
   - Parameters: ?robot, ?bowl
   - Preconditions: (not (inaction ?robot))
   - Effects: (at ?robot ?bowl), (not (inaction ?robot))

2. **PickupObject** (robot, bowl, bowl_location)
   - Parameters: ?robot, ?bowl, ?bowl_location
   - Preconditions: (at-location ?bowl ?bowl_location), (at ?robot ?bowl_location), (not (inaction ?robot))
   - Effects: (holding ?robot ?bowl), (not (inaction ?robot))

3. **GoToObject** (robot, box)
   - Parameters: ?robot, ?box
   - Preconditions: (not (inaction ?robot))
   - Effects: (at ?robot ?box), (not (inaction ?robot))

4. **PutObject** (robot, bowl, box)
   - Parameters: ?robot, ?bowl, ?box
   - Preconditions: (holding ?robot ?bowl), (at ?robot ?box), (not (inaction ?robot))
   - Effects: (at-location ?bowl ?box), (not (holding ?robot ?bowl)), (not (inaction ?robot))

## Parallel Execution Notes
- These subtasks can be executed in parallel by different robots
- If using one robot, Subtask 1 must complete before Subtask 2 since the bowl needs to be placed in the box which must first be on the sofa
- The box must be on the sofa before placing the bowl in it (sequential dependency)