(define (problem wash_knife_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    knife - object
    sink - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location knife counterTop)
    (at-location sink sink)
    (not (inaction robot2))
  )
  (:goal
    (and
      (cleaned robot2 knife)
      (at-location knife counterTop)
    )
  )
)