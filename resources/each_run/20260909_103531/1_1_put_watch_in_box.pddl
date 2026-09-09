(define (problem put_watch_in_box)
  (:domain robot2)
  (:objects
    robot2 - robot
    Watch - object
    Box - object
    SideTable - object
  )
  (:init
    (at robot2 SideTable)
    (at-location Watch SideTable)
    (at-location Box SideTable)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location Watch Box)
    )
  )
)