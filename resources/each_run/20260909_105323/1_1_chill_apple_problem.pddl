(define (problem chill_apple_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    apple - object
    fridge - object
    counterTop - object
  )
  (:init
    (at robot1 counterTop)
    (at-location apple counterTop)
    (at-location fridge counterTop)
    (object-close robot1 fridge)
    (not (inaction robot1))
  )
  (:goal
    (and
      (object-close robot1 fridge)
      (at-location apple fridge)
    )
  )
)