(define (problem turn_off_floor_lamp)
  (:domain robot2)
  (:objects
    robot2 - robot
    FloorLamp - object
    SideTable - object
  )
  (:init
    (at robot2 SideTable)
    (at-location FloorLamp SideTable)
    (not (inaction robot2))
  )
  (:goal
    (and
      (switch-off robot2 FloorLamp)
    )
  )
)