Here's the corrected PDDL plan with all 'variablelocation' references replaced by the actual variable names (objects) since they include location information, while maintaining proper PDDL syntax:

```
; Corrected plan for slicing apple and throwing it in trash
0.000: (gotoobject robot1 knife) [1.000]
1.000: (pickupobject robot1 knife countertop) [1.000]
1.000: (gotoobject robot1 apple) [1.000]
2.000: (pickupobject robot1 apple fruitbowl) [1.000]
2.000: (gotoobject robot1 cuttingboard) [1.000]
3.000: (sliceobject robot1 apple cuttingboard) [1.000]
3.000: (gotoobject robot1 garbagecan) [1.000]
4.000: (putobject robot1 apple garbagecan) [1.000]
```

Key changes made:
1. Removed all instances of 'variablelocation' and replaced them with the actual object names
2. Maintained proper PDDL plan format with timed durative actions
3. Kept the sequential execution flow while removing redundant robot2 actions
4. All actions are properly enclosed in parentheses as per PDDL requirements
5. Durations (in brackets) remain unchanged as they were correct

The plan now correctly references objects directly rather than through location variables, while maintaining all PDDL syntax requirements.