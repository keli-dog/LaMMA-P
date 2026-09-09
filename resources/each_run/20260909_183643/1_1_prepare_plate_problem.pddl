(define (problem prepare_plate_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    plate - object
    microwave - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location plate counterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location plate microwave)
    )
  )
)