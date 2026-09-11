(define (problem stage_lettuce_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    lettuce - object
    counterTop - object
    diningTable - object
  )
  (:init
    (at robot1 counterTop)
    (at-location lettuce diningTable)
    (not (inaction robot1))
  )
  (:goal
    (and
      (sliced lettuce)
      (at-location lettuce counterTop)
    )
  )
)