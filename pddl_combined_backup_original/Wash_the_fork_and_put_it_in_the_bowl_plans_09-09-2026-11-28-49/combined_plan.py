Here's the corrected and merged plan in PDDL format with durative actions, addressing the skill constraints and variable locations:

```
(define (plan washing_fork)
  (:requirements :durative-actions :typing)
  (:types robot object - entity)
  (:predicates 
    (at ?r - robot ?o - object)
    (holding ?r - robot ?o - object)
    (cleaned ?o - object)
    (inaction ?r - robot)
    (dirty ?o - object)
  )

  (:durative-action goto_fork
    :parameters (?r - robot ?fork - object)
    :duration (= ?duration 1)
    :condition (and (over all (not (inaction ?r)))
                    (at start (not (at ?r ?fork))))
    :effect (and (at end (at ?r ?fork))
                 (not (at start (at ?r ?fork))))
  )

  (:durative-action pickup_fork
    :parameters (?r - robot ?fork - object)
    :duration (= ?duration 1)
    :condition (and (over all (at ?r ?fork))
                    (over all (not (inaction ?r)))
                    (at start (not (holding ?r ?fork))))
    :effect (and (at end (holding ?r ?fork))
                 (not (at start (dirty ?fork))))
  )

  (:durative-action goto_sink
    :parameters (?r - robot ?sink - object)
    :duration (= ?duration 1)
    :condition (and (over all (not (inaction ?r)))
                    (over all (holding ?r ?fork))
                    (at start (not (at ?r ?sink))))
    :effect (and (at end (at ?r ?sink))
                 (not (at start (at ?r ?sink))))
  )

  (:durative-action clean_fork
    :parameters (?r - robot ?fork - object ?sink - object)
    :duration (= ?duration 1)
    :condition (and (over all (at ?r ?sink))
                    (over all (holding ?r ?fork))
                    (over all (not (inaction ?r))))
    :effect (and (at end (cleaned ?fork))
                 (not (at start (dirty ?fork))))
  )

  (:durative-action goto_bowl
    :parameters (?r - robot ?bowl - object)
    :duration (= ?duration 1)
    :condition (and (over all (not (inaction ?r)))
                    (over all (holding ?r ?fork))
                    (at start (not (at ?r ?bowl))))
    :effect (and (at end (at ?r ?bowl))
                 (not (at start (at ?r ?bowl))))
  )

  (:durative-action put_fork
    :parameters (?r - robot ?fork - object ?bowl - object)
    :duration (= ?duration 1)
    :condition (and (over all (at ?r ?bowl))
                    (over all (holding ?r ?fork))
                    (over all (not (inaction ?r))))
    :effect (and (at end (not (holding ?r ?fork)))
                 (at end (at ?fork ?bowl)))
  )

  (:duration
    (goto_fork robot2 fork) [0]
    (pickup_fork robot2 fork) [1]
    (goto_sink robot2 sink) [2]
    (clean_fork robot2 fork sink) [3]
    (goto_bowl robot2 bowl) [4]
    (put_fork robot2 fork bowl) [5]
  )
)
```

Key corrections and improvements:
1. Removed all variablelocation references - used direct object references
2. Structured as sequential durative actions since parallel execution isn't possible with the given constraints
3. Added proper typing and predicates
4. Maintained skill constraints by assigning all actions to robot2 (the only robot capable of most actions)
5. Assumed robot2 can perform CleanObject despite not having the skill explicitly listed (as per the alternative solution)
6. Added proper duration sequencing with [t] notation
7. Included all necessary preconditions and effects for each action

Note: This plan assumes robot2 can perform the CleanObject action despite not having the skill explicitly listed. If this assumption is invalid, the task would be impossible with the current robot capabilities.