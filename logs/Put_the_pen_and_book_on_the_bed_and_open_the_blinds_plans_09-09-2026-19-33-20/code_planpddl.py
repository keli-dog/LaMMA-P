Here's the corrected PDDL plan with all variablelocation references removed and only using the variable names themselves, as per your instructions:

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

The plan maintains all the original functionality and parallel execution structure while strictly following your requirements:
1. All "variablelocation" references have been removed
2. Only the variable names themselves are used (blinds, book, pen, bed)
3. The PDDL syntax is preserved with proper parenthesis usage
4. The timing and parallel execution structure remains unchanged
5. All actions reference the objects directly from the provided object list