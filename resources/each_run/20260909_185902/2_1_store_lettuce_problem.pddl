(define (problem store_lettuce_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    lettuce - object
    counterTop - object
    diningTable - object
  )
  (:init
    (at robot3 diningTable)
    (at-location lettuce diningTable)
    (not (inaction robot3))
  )
  (:goal
    (and
      (at-location lettuce counterTop)
    )
  )
)