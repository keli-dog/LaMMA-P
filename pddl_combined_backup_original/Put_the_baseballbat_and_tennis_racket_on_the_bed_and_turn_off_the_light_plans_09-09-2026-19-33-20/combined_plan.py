Here's the corrected and merged plan in PDDL format with timed durative actions for parallel execution:

```pddl
(define (plan task)
  (:method parallel_execution
    ; All three subtasks can run in parallel
    (:ordered
      (:task subtask1 :parameters (?robot1 - robot ?baseballbat - object ?bed - object))
      (:task subtask2 :parameters (?robot2 - robot ?tennisracket - object ?bed - object))
      (:task subtask3 :parameters (?robot3 - robot ?lightswitch - object))
    )
  )

  ; SubTask 1: Put Baseball Bat on Bed
  (:method subtask1
    (:sequence
      (0.0: (gotoobject ?robot1 ?baseballbat))
      (1.0: (pickupobject ?robot1 ?baseballbat))
      (2.0: (gotoobject ?robot1 ?bed))
      (3.0: (putobject ?robot1 ?baseballbat ?bed))
    )
  )

  ; SubTask 2: Put Tennis Racket on Bed
  (:method subtask2
    (:sequence
      (0.0: (gotoobject ?robot2 ?tennisracket))
      (1.0: (pickupobject ?robot2 ?tennisracket))
      (2.0: (gotoobject ?robot2 ?bed))
      (3.0: (putobject ?robot2 ?tennisracket ?bed))
    )
  )

  ; SubTask 3: Turn Off the Light
  (:method subtask3
    (:sequence
      (0.0: (gotoobject ?robot3 ?lightswitch))
      (1.0: (switchoff ?robot3 ?lightswitch))
    )
  )
)

; Actual parallel plan with timing
0.000: (gotoobject robot1 baseballbat) [1.0]
0.000: (gotoobject robot2 tennisracket) [1.0]
0.000: (gotoobject robot3 lightswitch) [1.0]
1.000: (pickupobject robot1 baseballbat) [1.0]
1.000: (pickupobject robot2 tennisracket) [1.0]
1.000: (switchoff robot3 lightswitch) [1.0]
2.000: (gotoobject robot1 bed) [1.0]
2.000: (gotoobject robot2 bed) [1.0]
3.000: (putobject robot1 baseballbat bed) [1.0]
3.000: (putobject robot2 tennisracket bed) [1.0]
```

Key corrections and improvements:
1. Removed all "variablelocation" references and used the objects directly
2. Structured the plan to show true parallel execution with timing information
3. All three subtasks start at time 0.0 and run concurrently
4. Each action has a duration of 1.0 time unit (adjustable as needed)
5. Maintained proper sequencing within each subtask while allowing parallel execution across subtasks
6. Used proper PDDL syntax with parameters and object typing
7. The plan shows the actual parallel execution with timing information at the bottom

The plan assumes:
- All robots start simultaneously
- Each action takes 1.0 time unit to complete
- Robots can move and act independently without collision (would need additional constraints in a real scenario)
- The objects (baseballbat, tennisracket, bed, lightswitch) are all properly defined in the domain