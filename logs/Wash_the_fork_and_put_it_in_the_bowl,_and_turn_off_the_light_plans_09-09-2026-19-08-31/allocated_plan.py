### SOLUTION

#### Task Analysis:
The task "Wash the fork and put it in the bowl, and turn off the light" consists of two independent subtasks that can be performed in parallel:
1. **SubTask 1**: Wash the fork and put it in the bowl (Skills: GoToObject, PickupObject, CleanObject, PutObject)
2. **SubTask 2**: Turn off the light (Skills: GoToObject, SwitchOff)

#### Robot Skills Analysis:
- **robot1**: ['GoToObject', 'BreakObject', 'ThrowObject'] → Cannot perform either subtask (missing Pickup/Put/SwitchOff)
- **robot2**: ['GoToObject', 'SwitchOn', 'SwitchOff'] → Can perform **SubTask 2** (Turn off light)
- **robot3**: ['GoToObject', 'PickupObject', 'PutObject'] → Can partially perform **SubTask 1** (missing CleanObject skill)

#### Problem Identified:
- **SubTask 1** requires cleaning the fork, but no robot has the `CleanObject` skill. This is a critical skill gap.
- Without `CleanObject`, the fork cannot be washed, making the task impossible to complete fully with the current robot team.

#### Possible Workarounds:
1. **Reformulate Task**: If "washing" is optional, robot3 could simply move the fork to the bowl (but this violates the task requirements).
2. **Add Robot with Cleaning Skill**: If another robot with `CleanObject` were available, it could team with robot3.

#### Conclusion:
The task **cannot be completed** with the given robots because:
- No robot has the `CleanObject` skill required for washing the fork.
- Even though robot2 can handle the light-switching subtask, the primary subtask (fork washing) is unachievable.

#### Optimal Allocation (Partial Completion):
If we ignore the cleaning requirement (though this violates the task description):
- **robot2**: Handle **SubTask 2** (Turn off light)
- **robot3**: Handle fork pickup and placement in bowl (without washing)
- **robot1**: Unused (no relevant skills)

However, this does not satisfy the original task requirements. The system should report **"Task impossible due to missing CleanObject skill"**.

#### Final Answer:
**Task cannot be allocated** - No robot possesses the required `CleanObject` skill for washing the fork. The minimum skill requirement for this task is not met by the available robots. 

Suggested actions:
1. Add a robot with `CleanObject` skill, or
2. Modify the task to remove the washing requirement. 

Current robot allocation (for partial completion):
- **robot2**: Turn off the light (SubTask 2)
- **robot3**: Pick up fork and place in bowl (without washing)
- **robot1**: Idle (no applicable skills).