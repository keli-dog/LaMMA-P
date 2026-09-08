(define (problem wash_lettuce_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    lettuce - object
    sink - object
    countertop - object
  )
  (:init
    (at robot2 countertop)
    (at-location lettuce countertop)
    (inaction robot2)
  )
  (:goal
    (and
      (cleaned lettuce)
    )
  )
)