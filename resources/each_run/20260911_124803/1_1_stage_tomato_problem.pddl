(define (problem stage_tomato_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    tomato - object
    counterTop - object
    fridge - object
  )
  (:init
    (at robot2 counterTop)
    (at-location tomato fridge)
  )
  (:goal
    (and
      (at-location tomato counterTop)
      (sliced tomato)
    )
  )
)