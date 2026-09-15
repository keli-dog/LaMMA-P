Here's the corrected and merged plan in PDDL format with durative actions, parallelization where possible, and proper variable handling:

```pddl
(define (plan place_laptop_on_bed)
  (:parameters
    (robot1 - robot)
    (laptop - object)
    (bed - object)
    (desk - object) ; assuming laptop starts on desk
  )
  
  (:durative-actions
    ; Action 1: Move to laptop and pick it up (sequential)
    (:durative-action goto_pickup_laptop
      :parameters (?r - robot ?o - object ?loc - object)
      :duration (= ?duration 5) ; example duration
      :condition (and
                  (at start (not (inaction ?r)))
                  (at start (at-location ?o ?loc))
                 )
      :effect (and
               (at end (at ?r ?loc))
               (at end (holding ?r ?o))
               (at end (not (at-location ?o ?loc)))
               (at end (not (inaction ?r)))
              )
    )
    
    ; Action 2: Move to bed and place laptop (sequential)
    (:durative-action goto_place_bed
      :parameters (?r - robot ?o - object ?b - object)
      :duration (= ?duration 7) ; example duration
      :condition (and
                  (at start (holding ?r ?o))
                  (at start (not (inaction ?r)))
                 )
      :effect (and
               (at end (at ?r ?b))
               (at end (at-location ?o ?b))
               (at end (not (holding ?r ?o)))
               (at end (not (inaction ?r)))
              )
    )
  )
  
  (:schedule
    ; Phase 1: Pickup laptop (t=0-5)
    (0: goto_pickup_laptop robot1 laptop desk)
    
    ; Phase 2: Place on bed (t=5-12)
    (5: goto_place_bed robot1 laptop bed)
  )
)
```

Key corrections and improvements:
1. Removed all 'variablelocation' references - using the objects directly which contain location information
2. Combined GoTo+Pickup and GoTo+Put into single durative actions since they must be sequential
3. Added proper PDDL syntax for durative actions with start/end conditions and effects
4. Included realistic durations for actions
5. Maintained proper parameter typing
6. Structured the plan with clear phases in the schedule
7. Ensured robot capacity requirements are met (robot1 is used as specified)

The plan is now properly parallelized where possible (though this simple task is mostly sequential) and follows PDDL conventions for durative actions. The schedule shows the timing of each action phase.