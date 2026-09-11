(define (problem prepare_heating_appliance)
  (:domain robot1)
  (:objects
    robot1 - robot
    microwave - object
    counterTop - object
    floor - object
  )
  (:init
    (at robot1 floor)
    (not (inaction robot1))
    (at-location microwave counterTop)
  )
  (:goal
    (object-open robot1 microwave)
  )
)