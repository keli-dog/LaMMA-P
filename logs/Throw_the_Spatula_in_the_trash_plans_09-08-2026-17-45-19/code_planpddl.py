The provided PDDL plan already follows the requirement of using the variable itself to represent its location. However, there are a few adjustments needed to ensure that the plan is correctly formatted and that all actions are properly defined. Here is the corrected PDDL plan:

```pddl
(define (problem throw_spatula)
  (:domain throw_spatula_domain)
  (:objects robot2 spatula trash)
  (:init
    (not (inaction robot2))
    (at spatula spatula) ; Corrected to use 'at' instead of 'at-location'
    (at trash trash) ; Corrected to use 'at' instead of 'at-location'
  )
  (:goal (and
    (not (holding robot2 spatula))
    (at robot2 trash)
  ))
  (:durative-action go_to_object
    :parameters (?robot ?object)
    :duration (= ?duration 1)
    :condition (and
      (at start (not (inaction ?robot)))
      (at end (at ?robot ?object))
    )
    :effect (and
      (at start (not (inaction ?robot)))
      (at end (not (inaction ?robot)))
    )
  )
  (:durative-action pickup_object
    :parameters (?robot ?object)
    :duration (= ?duration 1)
    :condition (and
      (at start (at ?robot ?object))
      (at start (not (inaction ?robot)))
      (at end (holding ?robot ?object))
    )
    :effect (and
      (at start (not (inaction ?robot)))
      (at end (not (inaction ?robot)))
    )
  )
  (:durative-action throw_object
    :parameters (?robot ?object)
    :duration (= ?duration 1)
    :condition (and
      (at start (holding ?robot ?object))
      (at start (not (inaction ?robot)))
      (at end (not (holding ?robot ?object)))
    )
    :effect (and
      (at start (not (inaction ?robot)))
      (at end (not (inaction ?robot)))
    )
  )
  (:durative-action plan
    :parameters (?robot ?spatula ?trash)
    :duration (= ?duration 4)
    :condition (and
      (at (interval 0 1) (go_to_object ?robot ?spatula))
      (at (interval 1 2) (pickup_object ?robot ?spatula))
      (at (interval 2 3) (go_to_object ?robot ?trash))
      (at (interval 3 4) (throw_object ?robot ?spatula))
    )
    :effect (and
      (at end (not (holding ?robot ?spatula)))
      (at end (at ?robot ?trash))
    )
  )
)
```

### Explanation of Changes:
1. **Initial State**: Changed `at-location` to `at` for consistency with the PDDL standard.
2. **Goal**: No changes needed.
3. **Durative Actions**: No changes needed as they already follow the correct format.
4. **Plan**: No changes needed as it correctly sequences the actions.

This plan now correctly represents the robot's actions in a PDDL format, ensuring that all actions are properly defined and that the robot's state transitions are accurately described.