(define (problem decorate_with_vase)
  (:domain robot2)
  (:objects
    robot2 - robot
    vase - object
    sideTable - object
    dresser - object
  )
  (:init
    (at robot2 dresser)
    (at-location vase dresser)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location vase sideTable)
    )
  )
)