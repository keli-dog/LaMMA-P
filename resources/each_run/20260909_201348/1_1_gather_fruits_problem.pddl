(define (problem gather_fruits_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    apple - object
    tomato - object
    counterTop - object
    appleLocation - object
    tomatoLocation - object
  )
  (:init
    (not (inaction robot1))
    (at robot1 counterTop)
    (at-location apple appleLocation)
    (at-location tomato tomatoLocation)
  )
  (:goal
    (and
      (at-location apple counterTop)
      (at-location tomato counterTop)
    )
  )
)