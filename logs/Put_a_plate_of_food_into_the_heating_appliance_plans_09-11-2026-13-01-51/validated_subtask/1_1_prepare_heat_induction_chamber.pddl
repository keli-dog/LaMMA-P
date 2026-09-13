(define (problem prepare_heat_induction_chamber)
  (:domain robot1)
  (:objects
    robot1 - robot
    microwave - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (inaction robot1)
    (at-location microwave counterTop)
  )
  (:goal
    (object-open robot1 microwave)
  )
)