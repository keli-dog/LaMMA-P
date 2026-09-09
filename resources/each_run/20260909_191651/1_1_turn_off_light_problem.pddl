(define (problem turn_off_light_problem)
  (:domain robot3)
  (:objects
    robot3 - robot
    LightSwitch Desk - object
  )
  (:init
    (at robot3 Desk)
    (at-location LightSwitch Desk)
    (switch-on robot3 LightSwitch)
    (not (inaction robot3))
  )
  (:goal
    (and
      (switch-off robot3 LightSwitch)
    )
  )
)