(define (problem pick_tomato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    tomato - object
    countertop - object
  )
  (:init
    (at robot1 countertop)
    (at-location tomato countertop)
    (inaction robot1)
  )
  (:goal
    (and
      (holding robot1 tomato)
    )
  )
)