Here's the corrected and merged plan in PDDL format with timed durative actions for parallel execution:

```pddl
(define (plan parallel_apple_fridge_light)
  (:time 0.0)
  
  ;; Parallel execution starts here
  ;; Robot1 handles apple and fridge tasks
  ;; Robot2 handles light switch tasks
  
  ;; Robot1's actions
  (:action (gotoobject robot1 apple) :duration 1.0 :start 0.0 :end 1.0)
  (:action (pickupobject robot1 apple) :duration 1.0 :start 1.0 :end 2.0)
  (:action (gotoobject robot1 fridge) :duration 1.0 :start 2.0 :end 3.0)
  (:action (openobject robot1 fridge) :duration 1.0 :start 3.0 :end 4.0)
  (:action (putobject robot1 apple fridge) :duration 1.0 :start 4.0 :end 5.0)
  (:action (closeobject robot1 fridge) :duration 1.0 :start 5.0 :end 6.0)
  
  ;; Robot2's actions (parallel with Robot1)
  (:action (gotoobject robot2 lightswitch) :duration 1.0 :start 0.0 :end 1.0)
  (:action (switchoff robot2 lightswitch) :duration 1.0 :start 1.0 :end 2.0)
  
  ;; Plan ends when all actions are complete
  (:time 6.0)
)
```

Key corrections and improvements made:
1. Removed all "variablelocation" references - using the objects directly (apple, fridge, lightswitch)
2. Structured the plan with proper PDDL syntax for timed durative actions
3. Maintained parallel execution where possible:
   - Robot1's first movement (to apple) happens simultaneously with Robot2's movement (to lightswitch)
   - Robot2 completes its task (switch off) by time 2.0 while Robot1 continues with fridge operations
4. Ensured proper sequencing within each robot's task chain
5. Added explicit start/end times for all actions
6. Total plan duration is 6.0 (determined by Robot1's longer sequence)

The plan satisfies all initial conditions and achieves both goals:
1. Apple is placed in the fridge (by Robot1)
2. Light is switched off (by Robot2)

Both robots work in parallel where possible without any resource conflicts or precondition violations.