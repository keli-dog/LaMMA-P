(define (problem switch_off_light_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    LightSwitch - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location LightSwitch counterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (switch-off robot1 LightSwitch)
    )
  )
)