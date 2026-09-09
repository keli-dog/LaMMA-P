# Task Decomposition: Put the book in the box and Turn on the mobile phone

## Analysis of Independent Subtasks
These are two completely independent tasks that can be performed in parallel by different robots:
1. SubTask 1: Put the book in the box (Skills: GoToObject, PickupObject, PutObject)
2. SubTask 2: Turn on the mobile phone (Skills: GoToObject, SwitchOn)

## Subtask 1: Put the book in the box

### Initial Conditions:
1. Robot not at book location
2. Robot not holding book
3. Box is at some location

### Action Sequence:

1. **GoToObject** (Robot, Book)
   - Parameters: ?robot - robot, ?book - object
   - Preconditions: (not (inaction ?robot))
   - Effects: (at ?robot ?book), (not (inaction ?robot))

2. **PickupObject** (Robot, Book, BookLocation)
   - Parameters: ?robot - robot, ?book - object, ?BookLocation - object
   - Preconditions: (at-location ?book ?BookLocation), (at ?robot ?BookLocation), (not (inaction ?robot))
   - Effects: (holding ?robot ?book), (not (inaction ?robot))

3. **GoToObject** (Robot, Box)
   - Parameters: ?robot - robot, ?box - object
   - Preconditions: (not (inaction ?robot))
   - Effects: (at ?robot ?box), (not (inaction ?robot))

4. **PutObject** (Robot, Book, Box)
   - Parameters: ?robot - robot, ?book - object, ?box - object
   - Preconditions: (holding ?robot ?book), (at ?robot ?box), (not (inaction ?robot))
   - Effects: (at-location ?book ?box), (not (holding ?robot ?book)), (not (inaction ?robot))

## Subtask 2: Turn on the mobile phone

### Initial Conditions:
1. Robot not at mobile phone location
2. Mobile phone is initially off

### Action Sequence:

1. **GoToObject** (Robot, MobilePhone)
   - Parameters: ?robot - robot, ?MobilePhone - object
   - Preconditions: (not (inaction ?robot))
   - Effects: (at ?robot ?MobilePhone), (not (inaction ?robot))

2. **SwitchOn** (Robot, MobilePhone)
   - Parameters: ?robot - robot, ?MobilePhone - object
   - Preconditions: (not (inaction ?robot)), (at ?robot ?MobilePhone)
   - Effects: (switch-on ?robot ?MobilePhone), (not (inaction ?robot))

## Parallel Execution Plan

We can assign these subtasks to different robots for parallel execution:

**Robot1:**
1. GoToObject(Robot1, Book)
2. PickupObject(Robot1, Book, BookLocation)
3. GoToObject(Robot1, Box)
4. PutObject(Robot1, Book, Box)

**Robot2:**
1. GoToObject(Robot2, MobilePhone)
2. SwitchOn(Robot2, MobilePhone)

This parallel execution will complete both tasks in the minimum time possible since there are no dependencies between the two subtasks.