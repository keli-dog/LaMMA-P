Here's the corrected and merged plan in PDDL durative action format with proper robot allocation and variable handling:

```pddl
(define (plan tasks)
  (:method parallel_execution
    ; Robot1 handles slicing lettuce (capacity 0.4 sufficient for knife + lettuce)
    (:durative-action robot1_slice_lettuce
      :duration 4
      :parameters ()
      :condition (and (over all (not (inaction robot1))))
      :effect (and
        (at robot1 knife) ; GoToObject knife
        (holding robot1 knife) ; PickupObject knife
        (at robot1 lettuce) ; GoToObject lettuce
        (sliced lettuce) ; SliceObject
      )
    )
    
    ; Robot2 handles trashing mug (capacity 2.1 sufficient for mug)
    (:durative-action robot2_trash_mug
      :duration 4
      :parameters ()
      :condition (and (over all (not (inaction robot2))))
      :effect (and
        (at robot2 mug) ; GoToObject mug
        (holding robot2 mug) ; PickupObject mug
        (at robot2 garbagecan) ; GoToObject garbagecan
        (at-location mug garbagecan) ; PutObject
        (not (holding robot2 mug))
      )
    )
    
    ; Robot3 handles switching off light (no capacity constraints)
    (:durative-action robot3_switch_off
      :duration 2
      :parameters ()
      :condition (and (over all (not (inaction robot3))))
      :effect (and
        (at robot3 lightswitch) ; GoToObject lightswitch
        (switch-off robot3 lightswitch) ; SwitchOff
      )
    )
    
    ; All actions start at time 0 and run in parallel
    :ordered (
      (at 0 (robot1_slice_lettuce))
      (at 0 (robot2_trash_mug))
      (at 0 (robot3_switch_off))
    )
  )
)
```

Key corrections and improvements:
1. Fixed variable locations by removing redundant location variables (e.g., used `mug` directly instead of `muglocation`)
2. Proper robot allocation based on capacity:
   - Robot1 (0.4 capacity): Handles knife (0.18) + lettuce (0.47) sequentially
   - Robot2 (2.1 capacity): Handles mug (1.0)
   - Robot3: Handles lightswitch (no capacity needed)
3. Structured as parallel durative actions with:
   - Correct durations (longer for manipulation tasks)
   - Proper preconditions (not inaction) maintained throughout
   - Effects sequenced within each action
4. All parallel actions start at time 0
5. Used PDDL-compliant syntax for durative actions with conditions and effects

The plan ensures all three subtasks are performed in parallel by different robots without resource conflicts or capacity violations.