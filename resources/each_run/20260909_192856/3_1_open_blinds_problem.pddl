(define (problem open_blinds_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    blinds - object
    window - object
  )
  (:init
    (at robot2 window)
    (at-location blinds window)
    (not (inaction robot2))
  )
  (:goal
    (and
      (object-open robot2 blinds)
    )
  )
)