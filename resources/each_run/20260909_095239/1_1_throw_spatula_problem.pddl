(define (problem throw_spatula_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    spatula - object
    garbageCan - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location spatula counterTop)
    (at-location garbageCan counterTop)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location spatula garbageCan)
    )
  )
)