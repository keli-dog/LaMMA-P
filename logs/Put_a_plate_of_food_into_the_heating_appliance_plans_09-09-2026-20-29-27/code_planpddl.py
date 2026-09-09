Here's the corrected PDDL plan with all 'variablelocation' references removed and using the objects directly, while maintaining proper PDDL syntax:

```pddl
(define (plan heat_food)
  (:parameters
    (robot1 - robot)
    (plate1 - object)
    (microwave1 - object)
    (counter1 - surface)
  )

  (:init
    (at plate1 counter1)
    (at microwave1 counter1)
    (at robot1 counter1)
    (not (holding robot1 anything))
    (not (open microwave1))
    (not (on microwave1))
    (not (inaction robot1))
  )

  (:durative-action goto_plate
    :parameters (?r - robot ?p - object ?loc - surface)
    :duration (= ?duration 2)
    :condition (and
                (at start (not (inaction ?r)))
                (at start (at ?p ?loc))
                (at start (at ?r ?loc))
               )
    :effect (and
              (at end (at ?r ?p))
              (at start (not (inaction ?r)))
            )
  )

  (:durative-action pickup_plate
    :parameters (?r - robot ?p - object ?loc - surface)
    :duration (= ?duration 3)
    :condition (and
                (over all (at ?r ?p))
                (at start (not (holding ?r anything)))
               )
    :effect (and
              (at end (holding ?r ?p))
              (at end (not (at ?p ?loc)))
            )
  )

  (:durative-action goto_microwave
    :parameters (?r - robot ?m - object)
    :duration (= ?duration 2)
    :condition (and
                (over all (holding ?r plate1))
                (at start (not (inaction ?r)))
               )
    :effect (and
              (at end (at ?r ?m))
              (at start (not (inaction ?r)))
            )
  )

  (:durative-action open_microwave
    :parameters (?r - robot ?m - object)
    :duration (= ?duration 2)
    :condition (and
                (over all (at ?r ?m))
                (at start (not (open ?m)))
               )
    :effect (and
              (at end (open ?m))
            )
  )

  (:durative-action put_in_microwave
    :parameters (?r - robot ?p - object ?m - object)
    :duration (= ?duration 3)
    :condition (and
                (over all (at ?r ?m))
                (over all (open ?m))
                (over all (holding ?r ?p))
               )
    :effect (and
              (at end (at ?p ?m))
              (at end (not (holding ?r ?p)))
            )
  )

  (:durative-action close_microwave
    :parameters (?r - robot ?m - object)
    :duration (= ?duration 2)
    :condition (and
                (over all (at ?r ?m))
                (over all (open ?m))
               )
    :effect (and
              (at end (not (open ?m)))
            )
  )

  (:durative-action switch_on_microwave
    :parameters (?r - robot ?m - object)
    :duration (= ?duration 1)
    :condition (and
                (over all (at ?r ?m))
                (at start (not (on ?m)))
               )
    :effect (and
              (at end (on ?m))
            )
  )

  (:schedule
    (0.0: goto_plate robot1 plate1 counter1)
    (2.0: pickup_plate robot1 plate1 counter1)
    (5.0: goto_microwave robot1 microwave1)
    (7.0: open_microwave robot1 microwave1)
    (9.0: put_in_microwave robot1 plate1 microwave1)
    (12.0: close_microwave robot1 microwave1)
    (14.0: switch_on_microwave robot1 microwave1)
  )
)
```

Key changes made:
1. Removed all 'variablelocation' references and used the objects directly
2. Simplified predicate names (e.g., 'object-open' → 'open', 'switch-on' → 'on')
3. Maintained consistent predicate naming throughout the plan
4. Kept the same action sequence and timing
5. Ensured all parameters and variables are properly referenced without location suffixes
6. Maintain