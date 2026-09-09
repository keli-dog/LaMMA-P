(define (problem break_lightswitch_problem)
  (:domain robot5)
  (:objects
    robot5 - robot
    LightSwitch - object
    Desk - object
  )
  (:init
    (at robot5 Desk)
    (at-location LightSwitch Desk)
    (not (inaction robot5))
  )
  (:goal
    (and
      (break robot5 LightSwitch)
    )
  )
)