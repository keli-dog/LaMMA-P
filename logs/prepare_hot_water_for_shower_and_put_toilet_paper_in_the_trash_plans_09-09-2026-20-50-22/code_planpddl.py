I'll modify the PDDL plan according to your instructions, correcting variable names to use the variable itself rather than redundant "location" references. Here's the corrected version:

```pddl
(define (plan household_tasks)
  (:durative-action robot2_prepare_hot_water
    :parameters (?robot2 - robot ?faucet - object ?bathtub - object)
    :duration (= ?duration 40)
    :condition (and
                (at start (not (inaction ?robot2)))
                (over all (not (inaction ?robot2))))
    :effect (and
             (at start (at ?robot2 ?faucet))
             (at start (switch-on ?robot2 ?faucet))
             (at 10 (at ?robot2 ?bathtub))
             (at end (switch-off ?robot2 ?faucet))
            )
  )

  (:durative-action robot3_dispose_toiletpaper
    :parameters (?robot3 - robot ?toiletpaper - object ?garbagecan - object)
    :duration (= ?duration 30)
    :condition (and
                (at start (not (inaction ?robot3)))
                (over all (not (inaction ?robot3)))
                (at start (at ?toiletpaper ?toiletpaper)))
    :effect (and
             (at start (holding ?robot3 ?toiletpaper))
             (at 10 (not (at ?toiletpaper ?toiletpaper)))
             (at 20 (at ?robot3 ?garbagecan))
             (at end (at ?toiletpaper ?garbagecan))
             (at end (not (holding ?robot3 ?toiletpaper)))
            )
  )

  (:parallel
    (robot2_prepare_hot_water robot2 faucet bathtub)
    (robot3_dispose_toiletpaper robot3 toiletpaper garbagecan)
  )
)
```

Key changes made:
1. Changed `(at-location ?toiletpaper ?toiletpaper)` to `(at ?toiletpaper ?toiletpaper)`
2. Changed `(not (at-location ?toiletpaper ?toiletpaper))` to `(not (at ?toiletpaper ?toiletpaper))`
3. Changed `(at-location ?toiletpaper ?garbagecan)` to `(at ?toiletpaper ?garbagecan)`

All other aspects of the plan remain unchanged, including the parallel execution structure, durations, and other conditions/effects. The plan maintains proper PDDL syntax with parentheses only used for the correct PDDL structure.