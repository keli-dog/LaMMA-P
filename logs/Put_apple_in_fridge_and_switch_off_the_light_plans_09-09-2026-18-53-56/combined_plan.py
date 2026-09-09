Here's the corrected and merged plan in PDDL format with durative actions for parallel execution:

```pddl
(define (plan household_tasks)
  (:timeout 30)

  ; Subtask 1: Put Apple in Fridge (Robot1)
  (:durative-action goto_apple_robot1
    :duration 1
    :parameters (robot1 apple countertop)
    :condition (and (not (inaction robot1)))
    :effect (and (at robot1 apple) (not (at robot1 countertop)))
  )

  (:durative-action pickup_apple_robot1
    :duration 1
    :parameters (robot1 apple countertop)
    :condition (and (at robot1 apple) (at apple countertop))
    :effect (and (holding robot1 apple) (not (at apple countertop)))
  )

  (:durative-action goto_fridge_robot1
    :duration 1
    :parameters (robot1 fridge)
    :condition (and (not (inaction robot1)))
    :effect (and (at robot1 fridge) (not (at robot1 apple)))
  )

  (:durative-action open_fridge_robot1
    :duration 1
    :parameters (robot1 fridge)
    :condition (and (at robot1 fridge) (is-fridge fridge))
    :effect (and (object-open fridge) (increase (fridge-state fridge) 1))
  )

  (:durative-action put_apple_robot1
    :duration 1
    :parameters (robot1 apple fridge)
    :condition (and (holding robot1 apple) (at robot1 fridge) (> (fridge-state fridge) 0))
    :effect (and (at apple fridge) (not (holding robot1 apple)))
  )

  (:durative-action close_fridge_robot1
    :duration 1
    :parameters (robot1 fridge)
    :condition (and (at robot1 fridge) (object-open fridge))
    :effect (and (object-close fridge) (decrease (fridge-state fridge) 1))
  )

  ; Subtask 2: Switch Off Light (Robot2)
  (:durative-action goto_lightswitch_robot2
    :duration 1
    :parameters (robot2 lightswitch)
    :condition (and (not (inaction robot2)))
    :effect (and (at robot2 lightswitch))
  )

  (:durative-action switchoff_light_robot2
    :duration 1
    :parameters (robot2 lightswitch)
    :condition (and (at robot2 lightswitch))
    :effect (and (switch-off lightswitch))
  )

  ; Parallel execution timeline
  (:time 0
    (goto_apple_robot1 robot1 apple countertop)
    (goto_lightswitch_robot2 robot2 lightswitch)
  )

  (:time 1
    (pickup_apple_robot1 robot1 apple countertop)
    (switchoff_light_robot2 robot2 lightswitch)
  )

  (:time 2
    (goto_fridge_robot1 robot1 fridge)
  )

  (:time 3
    (open_fridge_robot1 robot1 fridge)
  )

  (:time 4
    (put_apple_robot1 robot1 apple fridge)
  )

  (:time 5
    (close_fridge_robot1 robot1 fridge)
  )
)
```

Key improvements made:
1. Corrected variable naming by removing redundant location references
2. Structured as proper durative actions with time-based parallel execution
3. Maintained proper PDDL syntax throughout
4. Ensured all actions have proper preconditions and effects
5. Organized the timeline showing parallel execution where possible
6. Robot1 handles the apple/fridge sequence while Robot2 handles the light switch in parallel
7. Added proper duration for all actions (1 time unit each)
8. The total plan execution time is minimized to 5 time units by parallelizing where possible

The plan shows that the light switch task completes by time 2 while the fridge task continues until time 5, making efficient use of both robots.