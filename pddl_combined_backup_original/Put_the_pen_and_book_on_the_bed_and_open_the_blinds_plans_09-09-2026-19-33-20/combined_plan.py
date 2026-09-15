Here's the corrected and merged plan in PDDL format with timed durative actions, incorporating parallel execution where possible:

```
(define (plan household_tasks)
  (:time 0.0)
  
  ;; Parallel execution starts at time 0.0
  ;; Robot2 handles blinds (only robot with OpenObject capability)
  (:action (gotoobject robot2 blinds) :duration 1.0 :start 0.0)
  (:action (gotoobject robot4 book) :duration 1.0 :start 0.0)    ;; Robot4 handles book
  (:action (gotoobject robot1 pen) :duration 1.0 :start 0.0)     ;; Robot1 handles pen
  
  ;; After initial movement (time 1.0)
  (:action (openobject robot2 blinds) :duration 1.0 :start 1.0)
  (:action (pickupobject robot4 book) :duration 1.0 :start 1.0)
  (:action (pickupobject robot1 pen) :duration 1.0 :start 1.0)
  
  ;; After pickup (time 2.0)
  (:action (gotoobject robot4 bed) :duration 1.0 :start 2.0)
  (:action (gotoobject robot1 bed) :duration 1.0 :start 2.0)
  
  ;; After movement to bed (time 3.0)
  (:action (putobject robot4 book bed) :duration 1.0 :start 3.0)
  (:action (putobject robot1 pen bed) :duration 1.0 :start 3.0)
  
  ;; All tasks complete by time 4.0
)
```

Key corrections and improvements:
1. Removed all "variablelocation" references as instructed, using just the variable names
2. Assigned robots based on optimal allocation:
   - robot2 (only one with OpenObject) handles blinds
   - robot1 and robot4 handle pen and book in parallel
3. Structured as timed durative actions with explicit parallel execution
4. Maintained proper sequencing where dependencies exist (e.g., must pickup before putting down)
5. All actions have duration 1.0 for simplicity (can be adjusted to actual durations)
6. Total plan duration is 4.0 time units with maximum parallelization

The plan shows:
- From 0.0-1.0: All robots move to their first targets simultaneously
- From 1.0-2.0: Robots perform their first actions (opening/pickup)
- From 2.0-3.0: Robots move to bed
- From 3.0-4.0: Robots place items on bed

This achieves all three subtasks in minimal time through optimal parallelization.