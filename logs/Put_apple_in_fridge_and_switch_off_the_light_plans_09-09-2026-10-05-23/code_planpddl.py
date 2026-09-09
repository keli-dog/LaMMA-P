Here's the corrected PDDL plan with all variable locations and names properly modified to use the objects directly:

```pddl
(define (plan parallel_apple_fridge_light)
  (:time 0.0)
  
  ;; Parallel execution starts here
  ;; Robot1 handles apple and fridge tasks
  ;; Robot2 handles light switch tasks
  
  ;; Robot1's actions
  (:action (gotoobject robot1 Apple) :duration 1.0 :start 0.0 :end 1.0)
  (:action (pickupobject robot1 Apple) :duration 1.0 :start 1.0 :end 2.0)
  (:action (gotoobject robot1 Fridge) :duration 1.0 :start 2.0 :end 3.0)
  (:action (openobject robot1 Fridge) :duration 1.0 :start 3.0 :end 4.0)
  (:action (putobject robot1 Apple Fridge) :duration 1.0 :start 4.0 :end 5.0)
  (:action (closeobject robot1 Fridge) :duration 1.0 :start 5.0 :end 6.0)
  
  ;; Robot2's actions (parallel with Robot1)
  (:action (gotoobject robot2 LightSwitch) :duration 1.0 :start 0.0 :end 1.0)
  (:action (switchoff robot2 LightSwitch) :duration 1.0 :start 1.0 :end 2.0)
  
  ;; Plan ends when all actions are complete
  (:time 6.0)
)
```

Key modifications made:
1. Changed 'apple' to 'Apple' (matching the exact object name from the list)
2. Changed 'fridge' to 'Fridge' (matching the exact object name from the list)
3. Changed 'lightswitch' to 'LightSwitch' (matching the exact object name from the list)
4. All object names now exactly match their capitalization and spelling from the provided object list
5. Maintained all other aspects of the original plan including timing and parallel execution structure

The plan remains valid with these corrections as all object references now exactly match the available objects in the environment.