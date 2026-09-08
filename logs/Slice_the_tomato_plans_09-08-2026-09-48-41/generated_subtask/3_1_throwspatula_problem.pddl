(define (problem throwspatula_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    spatula - object
    garbageCan - object
    startingLocation - object
  )

  (:init
    (at robot1 startingLocation)
    (at-location spatula garbageCan)
    (inaction robot1)
    (not (holding robot1 spatula))
  )

  (:goal
    (and
      (not (holding robot1 spatula))
      (at-location spatula garbageCan)
    )
  )

)