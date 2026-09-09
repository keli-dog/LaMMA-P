### SOLUTION

#### Analysis of Robots and Tasks:
1. **Robot Capabilities**:
   - **robot1**: Has all required skills for both subtasks (GoToObject, PickupObject, SliceObject, PutObject, OpenObject, CloseObject)
   - **robot2**: Missing PickupObject and PutObject skills, which are essential for handling objects

2. **Object Mass Considerations**:
   - All objects involved (Potato: 0.18, Knife: 0.18, Fridge: 0.0) are well below both robots' mass capacity (100)
   - No mass constraints prevent either robot from handling these objects

3. **Task Requirements**:
   - Both subtasks require object manipulation skills (PickupObject/PutObject) that only robot1 possesses
   - The tasks must be performed sequentially (slice before storing)

#### Optimal Allocation:
Since only robot1 has all required skills for both subtasks, the entire operation must be performed by robot1:

1. **robot1 performs all actions sequentially**:
   - Subtask 1 (Slice Potato):
     - GoToObject(Knife)
     - PickupObject(Knife)
     - GoToObject(Potato)
     - SliceObject(Potato)
   - Subtask 2 (Store in Fridge):
     - PutObject(Knife, CounterTop) [put down knife]
     - PickupObject(Potato)
     - GoToObject(Fridge)
     - OpenObject(Fridge)
     - PutObject(Potato, Fridge)
     - CloseObject(Fridge)

2. **robot2** cannot assist meaningfully as it lacks PickupObject/PutObject skills. It could only perform GoToObject operations, which wouldn't help complete the task.

#### Why This Allocation Works:
- Satisfies all skill requirements (only robot1 has full skill set)
- Meets mass capacity constraints (all objects are lightweight)
- Maintains proper task sequencing
- Uses minimum number of robots (1) since the task cannot be parallelized without the second robot having pickup/put skills

#### Alternative Consideration:
If we had a third robot with PickupObject/PutObject skills, we could potentially parallelize some operations (e.g., one robot slices while another prepares the fridge), but with the given robots, serial execution by robot1 is the only viable solution.

### Final Answer:
Assign the entire task sequence to robot1, as it's the only robot with all required skills (PickupObject and PutObject). Robot2 cannot meaningfully contribute due to missing essential object manipulation skills. The task will be completed sequentially by robot1 performing all slicing and storing operations.