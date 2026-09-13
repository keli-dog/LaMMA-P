(define (problem close_heat_induction_chamber)
  (:domain robot1)
  (:objects
    robot1 - robot
    microwave - object
    countertop - object
  )
  (:init
    (at robot1 countertop)
    (at-location microwave countertop)
  )
  (:goal
    (object-close robot1 microwave)
  )
)