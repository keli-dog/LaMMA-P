(define (problem place_tomato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    tomato - object
    counterTop - object
    shelf - object
  )
  (:init
    (at robot1 shelf)
    (at-location tomato shelf)
    (not (inaction robot1))
  )
  (:goal
    (and
      (at-location tomato counterTop)
    )
  )
)