### SOLUTION

#### Analysis:
1. **Robot Capabilities**:
   - Both robots (robot1 and robot2) have identical skill sets and mass capacities (100 units).
   - All required skills for both subtasks are available in both robots.

2. **Object Mass**:
   - Apple: 0.2 units
   - Knife: 0.18 units
   - Fridge: 0 units (static object)
   - Sink: 0 units (static object)
   - All objects involved are well within the mass capacity of either robot.

3. **Parallel Execution**:
   - The two subtasks ("Chill the apple" and "Wash the knife") are independent and can be performed in parallel.
   - Each subtask can be assigned to a separate robot for maximum efficiency.

#### Task Allocation:
- **SubTask 1: Chill the Apple** → Assign to robot1
- **SubTask 2: Wash the Knife** → Assign to robot2

#### Justification:
1. **Skills Coverage**:
   - Both robots have all required skills for their respective tasks:
     - Chill apple: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
     - Wash knife: GoToObject, PickupObject, CleanObject, PutObject

2. **Mass Capacity**:
   - The heaviest object being manipulated is the apple (0.2 units) and knife (0.18 units), which are negligible compared to the robots' 100-unit capacity.

3. **Efficiency**:
   - Parallel execution reduces total task completion time.
   - No need for robot coordination or team formation since tasks are independent.

4. **Redundancy**:
   - If one robot fails, the other could complete both tasks sequentially (though this would be less efficient).

#### Alternative Consideration:
If only one robot were available, the tasks would need to be performed sequentially by that single robot, taking approximately twice as long to complete both tasks.

#### Final Allocation:
- **robot1**: 
  - GoToObject(Apple)
  - PickupObject(Apple)
  - GoToObject(Fridge)
  - OpenObject(Fridge)
  - PutObject(Apple, Fridge)
  - CloseObject(Fridge)

- **robot2**:
  - GoToObject(Knife)
  - PickupObject(Knife)
  - GoToObject(Sink)
  - CleanObject(Knife)
  - PutObject(Knife, [CleanLocation])

This allocation satisfies all constraints while maximizing efficiency through parallel execution.