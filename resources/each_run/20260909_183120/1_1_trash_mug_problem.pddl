(define (problem trash_mug_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    mug - object
    garbageCan - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location mug counterTop)
    (at-location garbageCan counterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at-location mug garbageCan)
    )
  )
)