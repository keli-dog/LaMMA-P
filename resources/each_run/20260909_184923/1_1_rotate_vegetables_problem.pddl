(define (problem rotate_vegetables_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    lettuce - object
    tomato - object
    counterTop - object
  )
  (:init
    (at robot2 counterTop)
    (at-location lettuce counterTop)
    (at-location tomato counterTop)
    (not (inaction robot2))
  )
  (:goal
    (and
      (at robot2 lettuce)
      (rotation-count 3)
    )
  )
)