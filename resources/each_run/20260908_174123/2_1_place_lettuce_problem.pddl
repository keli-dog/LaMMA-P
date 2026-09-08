(define (problem place_lettuce_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    lettuce - object
    countertop - object
    drawer - object
  )
  (:init
    (at robot2 countertop)
    (at-location lettuce drawer)
    (inaction robot2)
  )
  (:goal
    (and
      (at-location lettuce countertop)
    )
  )
)