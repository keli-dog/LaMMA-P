I'll modify the provided PDDL plan to correct the variable references as requested, ensuring that all 'variablelocation' instances are replaced with the variable itself (since the variable includes location) and that variable names are properly referenced. Here's the corrected plan:

```pddl
(define (plan throw_spatula_in_trash)
  (:action GoToObject_Spatula
    :parameters (robot1 Spatula)
    :duration (= ?duration 5)
    :condition (and (over all (not (inaction robot1)))
                    (at start (not (holding robot1 Spatula))))
    :effect (and (at end (at robot1 Spatula))
                 (at start (not (inaction robot1)))
                 (at end (not (inaction robot1))))
  )

  (:action PickupObject_Spatula
    :parameters (robot1 Spatula)
    :duration (= ?duration 3)
    :condition (and (over all (at robot1 Spatula))
                    (over all (not (inaction robot1)))
                    (at start (not (holding robot1 Spatula))))
    :effect (and (at end (holding robot1 Spatula))
                 (at end (not (at Spatula)))
                 (at start (not (inaction robot1)))
                 (at end (not (inaction robot1))))
  )

  (:action GoToObject_GarbageCan
    :parameters (robot1 GarbageCan)
    :duration (= ?duration 5)
    :condition (and (over all (holding robot1 Spatula))
                    (over all (not (inaction robot1))))
    :effect (and (at end (at robot1 GarbageCan))
                 (at start (not (inaction robot1)))
                 (at end (not (inaction robot1))))
  )

  (:action PutObject_Spatula
    :parameters (robot1 Spatula GarbageCan)
    :duration (= ?duration 2)
    :condition (and (over all (holding robot1 Spatula))
                    (over all (at robot1 GarbageCan))
                    (over all (not (inaction robot1))))
    :effect (and (at end (at Spatula GarbageCan))
                 (at end (not (holding robot1 Spatula)))
                 (at start (not (inaction robot1)))
                 (at end (not (inaction robot1))))
  )

  (:method perform_throw
    :parameters (robot1 Spatula GarbageCan)
    :subtasks (and
      (task1 :action (GoToObject_Spatula robot1 Spatula))
      (task2 :action (PickupObject_Spatula robot1 Spatula))
      (task3 :action (GoToObject_GarbageCan robot1 GarbageCan))
      (task4 :action (PutObject_Spatula robot1 Spatula GarbageCan))
    )
    :ordering (and
      (task1 < task2)
      (task2 < task3)
      (task3 < task4)
    )
  )
)
```

Key changes made:
1. Replaced all instances of "at-location" with "at" since the variable itself includes location information
2. Maintained proper PDDL syntax throughout
3. Kept all other aspects of the plan intact including durations, conditions, and effects
4. Ensured the method structure and ordering constraints remain unchanged
5. Verified all object references match the provided object list

The plan now correctly references locations through the objects themselves rather than through separate location variables, while maintaining all the original functionality.