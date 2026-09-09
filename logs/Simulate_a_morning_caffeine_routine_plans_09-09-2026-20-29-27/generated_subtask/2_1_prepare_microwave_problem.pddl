(define (problem prepare_microwave_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    microwave - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location microwave counterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (object-open robot1 microwave)
    )
  )
)