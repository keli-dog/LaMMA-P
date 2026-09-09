(define (problem adjust_lighting_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    LightSwitch - object
    SideTable - object
  )
  (:init
    (at robot2 SideTable)
    (at-location LightSwitch SideTable)
    (not (inaction robot2))
  )
  (:goal
    (and
      (switch-on robot2 LightSwitch)
    )
  )
)