Based on the task requirements and robot capabilities, here's the optimal allocation for washing a fork and putting it in a bowl:

### Task Analysis:
1. **Required Skills**: GoToObject, PickupObject, CleanObject, PutObject
2. **Sequence**: Strictly sequential (each step depends on the previous one)
3. **Mass Considerations**: All objects involved (fork, sink, bowl) have negligible mass (<1), well within any robot's capacity

### Robot Capabilities:
- robot1: ['GoToObject', 'SwitchOn', 'SwitchOff'] → Missing PickupObject, CleanObject, PutObject
- robot2: ['GoToObject', 'PickupObject', 'PutObject'] → Missing CleanObject
- robot3: ['GoToObject', 'BreakObject', 'ThrowObject'] → Missing PickupObject, CleanObject, PutObject

### Solution:
Since none of the robots have the CleanObject skill, we have two options:

1. **Partial Solution (without cleaning)**:
   - Assign robot2 to perform all steps except cleaning:
     - GoToObject(Fork)
     - PickupObject(Fork)
     - GoToObject(Bowl)
     - PutObject(Fork, Bowl)
   - This would move the fork but not clean it

2. **Team Solution (if CleanObject can be improvised)**:
   - robot2 (primary worker):
     - GoToObject(Fork)
     - PickupObject(Fork)
     - GoToObject(Sink)
   - robot1 (assistant for cleaning):
     - GoToObject(Sink)
     - Use SwitchOn to activate water flow (if applicable)
   - robot2:
     - PutObject(Fork, Bowl)

### Optimal Allocation:
Given the constraints, the best possible solution is to assign robot2 to perform all possible steps (without cleaning), as it's the only robot with PickupObject and PutObject skills. The cleaning step cannot be properly executed with the current robot capabilities.

### Final Allocation:
```
robot2:
1. GoToObject(Fork)
2. PickupObject(Fork)
3. GoToObject(Bowl)
4. PutObject(Fork, Bowl)
```

Note: This solution moves the fork to the bowl but doesn't clean it. To fully complete the original task, a robot with CleanObject capability would be required.